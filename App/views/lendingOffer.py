from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash,Response
from flask_login import login_required, current_user, LoginManager
from werkzeug.utils import secure_filename

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
    findItems
)

lendingOffer_views = Blueprint('lendingOffer_views', __name__, template_folder='../templates')

#Route to capture lending offer data and create a lending offer object
@lendingOffer_views.route('/createLendingOfferPage',methods=['POST'])
@login_required
def makeOfferPage():
    data=request.form
    pic=request.files["image"]
    itemPic=secure_filename(pic.filename)
    mimetype=pic.mimetype
    itemPic=pic.read()
    itemPicName=itemPic
    offer=create_lendingOffer(current_user.id,data['item'],data['category'],data['itemDescription'],itemPic,itemPicName,mimetype,data['rulesOfUse'],data['condition'],data['preferedLocation'])
    print(offer.item)
    return redirect(url_for('user_views.gethomepage'))

@lendingOffer_views.route('/searchItem',methods=['GET'])
@login_required
def lookup():
    data=request.values
    results=findItems(data['userInput'])
    return results

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
    #data=request.form
    data=remove_Offer(id)
    offer=get_offer_by_ID(id)
    return jsonify(offer)

#Route to retrieve all lending offers by category
@lendingOffer_views.route('/GetCategoryOffers/<category>',methods=['GET'])
@login_required
def GetCategoryOffers(category):

    offers=getItmesByCategory(category)
    print(offers)
    print(category)
    selection=category
    return render_template('homepage.html', selection=selection, offers=offers)

@lendingOffer_views.route('/AddDatesPage/<lendingRequestID>/<lendingoffer_ID>',methods=['GET'])
@login_required
def InputDatesPage(lendingRequestID,lendingoffer_ID):
    return render_template('',lendingRequestID=lendingRequestID,lendingoffer_ID=lendingoffer_ID)

@lendingOffer_views.route('/AddDates/<lendingRequestID>/<borrowerID>/<lendingoffer_ID>',methods=['PUT'])
@login_required
def InputDates(lendingRequestID,borrowerID,lendingoffer_ID):
    data=request.form
    offer=setDates(lendingoffer_ID,lendingRequestID,data['returnDate'],data['borrowDate'])
    #return jsonify(offer.returnDate)
    return redirect(url_for('manager_views.TransmitList',lendingoffer_ID=lendingoffer_ID))

@lendingOffer_views.route('/RemoveLendingOffer<id>',methods=['POST'])
def DeleteOffer(id):
    data=remove_Offer(id)
    return jsonify(data)

@lendingOffer_views.route('/GetAllOffers', methods=['GET'])
@login_required
def RetreiveAllOffers():
    offers=getAllOffersJSON()
    return offers

@lendingOffer_views.route('/GetAllUserOffers', methods=['GET'])
@login_required
def RetreiveAllUserOffers():
    offers=getAllUserOffers(current_user.id)
    return offers

#TESTING ROUTES
#Route to test retrieving offers by a category
@lendingOffer_views.route('/testGetCategoryOffers',methods=['GET'])
@login_required
def testGetCategoryOffers():
    data=request.json
    offers=getItmesByCategory(data['category'])
    return offers

#Route to test create lending offer 
@lendingOffer_views.route('/testCreateLendingOfferPage',methods=['POST'])
@login_required
def testMakeOfferPage():
    data=request.json#must change json to form for web page
    offer=create_lendingOffer(data['lenderID'],data['item'],data['category'],data['itemDescription'],data['itemPic'],data['itemPicName'],data['mimetype'],data['rulesOfUse'],data['condition'],data['preferedLocation'])
    return jsonify(offer.item)

@lendingOffer_views.route('/testAddDates/<lendingRequestID>',methods=['PUT'])
@login_required
def testInputDates(lendingRequestID):
    data=request.json
    offer=setDates(data['id'],data['lendingRequestID'],data['returnDate'],data['borrowDate'])
    return jsonify(offer.returnDate)

#Route to test updating a lending offer
@lendingOffer_views.route('/testUpdateLendingOffer<OfferID>',methods=['PUT'])
@login_required
def testChangeOffer(OfferID):
    data=request.json#must change json to form for web page
    offer=update_Offer(data['OfferID'],data['item'],data['category'],data['itemDescription'],data['itemPic'],data['itemPicName'],data['mimetype'],data['rulesOfUse'],data['condition'],data['preferedLocation'])
    return jsonify(offer.item)

#Route to test deleting a lending offer
@lendingOffer_views.route('/testRemoveLendingOffer<id>',methods=['POST'])
def testDeleteOffer(id):
    data=request.json
    data=remove_Offer(data['id'])
    offer=get_offer_by_ID(id)
    return jsonify(offer)

#Route to test retrieving all lending offers
@lendingOffer_views.route('/testGetAllOffers', methods=['GET'])
@login_required
def testRetreiveAllOffers():
    offers=getAllOffersJSON()
    return offers

