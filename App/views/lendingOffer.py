from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash,Response
from flask_login import login_required, current_user, LoginManager
from werkzeug.utils import secure_filename
import json

from App.controllers import (
    create_lendingOffer, 
    get_offer_by_ID,
    get_lender,
    get_all_offers,
    update_Offer,
    remove_Offer,
    getAllOffersJSON,
    getItmesByCategory,
    setDates,
    getAllUserOffers,
    findItems,
    uploadItem,
    restartOffer,
    getApprovedRequest,
    getAllBorrowingDays,
    changeIsReturned
)

lendingOffer_views = Blueprint('lendingOffer_views', __name__, template_folder='../templates')

#Route to capture lending offer data and create a lending offer object
@lendingOffer_views.route('/createLendingOfferPage',methods=['POST'])
@login_required
def makeOfferPage():
    data=request.form
    pic=request.files["image"]
    itemPic=secure_filename(pic.filename)
    #Uploading image to firebase code 
    if(pic):
        imageURL = uploadItem(pic, itemPic)
    else:
        imageURL = '/static/images/no-image.svg'

    offer=create_lendingOffer(current_user.id,data['item'],data['category'],data['itemDescription'],imageURL,data['rulesOfUse'],data['condition'],data['preferedLocation'])
    flash('You have successfully added a new item')
    return redirect(url_for('user_views.gethomepage'))

@lendingOffer_views.route('/searchItem',methods=['GET'])
@login_required
def lookup():
    data=request.values
    results=findItems(data['userInput'])
    search = data['userInput']
    return render_template('homepage.html', selection=None, offers=results, search=search, user=current_user)

@lendingOffer_views.route('/addItem', methods=['GET'])
@login_required
def getLendingOfferPage():
    return render_template('addNewItem.html')

@lendingOffer_views.route('/updateLendingOfferPage<OfferID>',methods=['GET'])
@login_required
def changeOfferPage(OfferID):
    offer=get_offer_by_ID(OfferID)
    return render_template('addNewItem.hmtl',offer=offer)

#Route to capture new lending offer data and update users lending offer
@lendingOffer_views.route('/updateLendingOffer<OfferID>',methods=['PUT'])
@login_required
def changeOffer(OfferID):
    data=request.form
    offer=update_Offer(data['OfferID'],data['item'], data['category'],data['condition'],data['preferedLocation'],data['rulesOfUse'])
    return jsonify(offer.item)

#Route to delete a lending offer
@lendingOffer_views.route('/removeLendingOffer<id>',methods=['POST'])
def deleteOffer(id):
    data=remove_Offer(id)
    offer=get_offer_by_ID(id)
    flash('Lending Offer has been successfully deleted. ')
    return redirect(url_for('lendingOffer_views.RetreiveAllUserOffers'))

#Route to retrieve all lending offers by category
@lendingOffer_views.route('/GetCategoryOffers/<category>',methods=['GET'])
@login_required
def GetCategoryOffers(category):
    offers=getItmesByCategory(category)
    selection=category
    return render_template('homepage.html', selection=selection, offers=offers, search=None, user=current_user)

@lendingOffer_views.route('/AddDatesPage/<lendingRequestID>/<lendingoffer_ID>',methods=['GET'])
@login_required
def InputDatesPage(lendingRequestID,lendingoffer_ID):
    return render_template('',lendingRequestID=lendingRequestID,lendingoffer_ID=lendingoffer_ID)

@lendingOffer_views.route('/AddDates/<lendingRequestID>/<borrowerID>/<lendingoffer_ID>',methods=['PUT'])
@login_required
def InputDates(lendingRequestID,borrowerID,lendingoffer_ID):
    data=request.form
    offer=setDates(lendingoffer_ID,lendingRequestID,data['returnDate'],data['borrowDate'])
    return redirect(url_for('manager_views.TransmitList',lendingoffer_ID=lendingoffer_ID))

@lendingOffer_views.route('/RemoveLendingOffer<id>',methods=['POST'])
def DeleteOffer(id):
    data=remove_Offer(id)
    return jsonify(data)

@lendingOffer_views.route('/GetAllOffers', methods=['GET'])
@login_required
def RetreiveAllOffers():
    offers=getAllOffersJSON()
    return jsonify(offers)

@lendingOffer_views.route('/GetAllUserOffers', methods=['GET'])
@login_required
def RetreiveAllUserOffers():
    offers=getAllUserOffers(current_user.id)
    borrowingDays = getAllBorrowingDays()
    return render_template('myLendingOffers.html', offers=offers)

@lendingOffer_views.route('/RestartOffer/<lendingoffer_ID>',methods=['GET'])
@login_required
def Restart(lendingoffer_ID):
    offer=restartOffer(current_user.id,lendingoffer_ID)
    flash('Your offer has been successfully restarted. Any associated requests have been removed, and it will be re-displayed on the All Items Page.')
    return redirect(url_for('lendingOffer_views.RetreiveAllUserOffers'))

@lendingOffer_views.route('/CheckisReturned/<lendingOfferID>', methods=['GET'])
@login_required
def CheckisReturned(lendingOfferID):
    lendingOffer=changeIsReturned(lendingOfferID,current_user.id)
    flash('Item was successfully returned.')
    return redirect(url_for('lendingOffer_views.RetreiveAllUserOffers'))

#TESTING ROUTES
#Route to test retrieving offers by a category
@lendingOffer_views.route('/testGetCategoryOffers',methods=['GET'])
@login_required
def testGetCategoryOffers():
    data=request.json
    offers=getItmesByCategory(data['category'])
    return jsonify(offers[1])

#Route to test create lending offer 
@lendingOffer_views.route('/testCreateLendingOfferPage',methods=['POST'])
@login_required
def testMakeOfferPage():
    data=request.json#must change json to form for web page
    pic=request.json['imageURL']
    pic=None
    #Uploading image to firebase code 
    if(pic):
        imageURL = uploadItem(pic, itemPic)
    else:
        imageURL = '/static/images/no-image.svg'

    offer=create_lendingOffer(current_user.id,data['item'],data['category'],data['itemDescription'],imageURL,data['rulesOfUse'],data['condition'],data['preferedLocation'])
    flash('You have successfully added a new item')
    return jsonify(offer.toJSON(),"Lending Offer Created")


@lendingOffer_views.route('/TestAddDates',methods=['PUT'])
@login_required
def TestInputDates():
    data=request.json
    offer=setDates(data['lendingoffer_ID'],data['lendingRequestID'],data['returnDate'],data['borrowDate'])
    print(offer)
    return jsonify(offer.returnDate, "Dates Added")

#Route to test updating a lending offer
@lendingOffer_views.route('/testUpdateLendingOffer/<OfferID>',methods=['PUT'])
@login_required
def testChangeOffer(OfferID):
    data=request.json#must change json to form for web page
    offer=update_Offer(data['OfferID'],data['item'],data['category'],data['itemDescription'],data['imageURL'],data['rulesOfUse'],data['condition'],data['preferedLocation'])
    return jsonify(offer.toJSON(), "Lending Offer Data Updated")

#Route to test deleting a lending offer
@lendingOffer_views.route('/testRemoveLendingOffer/<id>',methods=['POST'])
def testDeleteOffer(id):
    data=request.json
    data=remove_Offer(data['id'])
    return jsonify("Lending Offer Removed")

#Route to test retrieving all lending offers
@lendingOffer_views.route('/testGetAllOffers', methods=['GET'])
@login_required
def testRetreiveAllOffers():
    offers=getAllOffersJSON()
    return jsonify(offers)

@lendingOffer_views.route('/TestGetAllUserOffers', methods=['GET'])
@login_required
def testRetreiveAllUserOffers():
    offers=getAllUserOffers(current_user.id)  
    return jsonify(offers[1]['item'],offers[2]['item'],offers[3]['item'],"All User Items Offers Displayed")

@lendingOffer_views.route('/testRestartOffer',methods=['PUT'])
@login_required
def testRestart():
    data=request.json
    offer=restartOffer(current_user.id,data['lendingoffer_ID'])
    return jsonify(offer)


@lendingOffer_views.route('/testCheckisReturned', methods=['PUT'])
@login_required
def testCheckisReturned():
    data=request.json
    lendingRequest=changeIsReturned(data['id'],current_user.id)
    return jsonify("Item Has Been Returned")

@lendingOffer_views.route('/testSearchItem',methods=['GET'])
@login_required
def testLookup():
    data=request.json
    results=findItems(data['userInput'])
    return jsonify(results)