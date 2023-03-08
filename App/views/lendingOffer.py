from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager

from App.controllers import (
    create_lendingOffer, 
    get_offer_by_ID,
    get_lender,
    get_all_offers,
    update_Offer,
    remove_Offer,
    getAllOffersJSON
)

lendingOffer_views = Blueprint('lendingOffer_views', __name__, template_folder='../templates')


@lendingOffer_views.route('/createLendingOfferPage',methods=['POST'])
@login_required
def makeOfferPage():
    data=request.form#must change json to form for web page
    offer=create_lendingOffer(data['lenderID'],data['item'],data['condition'],data['preferedLocation'],data['Status'],data['rulesOfUse'])
    print(offer.item)
    return jsonify(offer.item)

@lendingOffer_views.route('/updateLendingOffer<OfferID>',methods=['PUT'])
@login_required
def changeOffer(OfferID):
    data=request.form#must change json to form for web page
    offer=update_Offer(data['OfferID'],data['item'],data['condition'],data['preferedLocation'],data['Status'],data['rulesOfUse'])
    return jsonify(offer.item)

@lendingOffer_views.route('/removeLendingOffer<id>',methods=['POST'])
def deleteOffer(id):
    data=request.form
    data=remove_Offer(data['id'])
    offer=get_offer_by_ID(id)
    return jsonify(offer)

#TESTING ROUTES
@lendingOffer_views.route('/testCreateLendingOfferPage',methods=['POST'])
@login_required
def testMakeOfferPage():
    data=request.json#must change json to form for web page
    offer=create_lendingOffer(data['lenderID'],data['item'],data['condition'],data['preferedLocation'],data['Status'],data['rulesOfUse'])
    print(offer.item)
    return jsonify(offer.item)

@lendingOffer_views.route('/testUpdateLendingOffer<OfferID>',methods=['PUT'])
@login_required
def testChangeOffer(OfferID):
    data=request.json#must change json to form for web page
    offer=update_Offer(data['OfferID'],data['item'],data['condition'],data['preferedLocation'],data['Status'],data['rulesOfUse'])
    return jsonify(offer.item)

@lendingOffer_views.route('/testRemoveLendingOffer<id>',methods=['POST'])
def testDeleteOffer(id):
    data=request.json
    data=remove_Offer(data['id'])
    offer=get_offer_by_ID(id)
    return jsonify(offer)

@lendingOffer_views.route('/testGetAllOffers', methods=['GET'])
@login_required
def testRetreiveAllOffers():
    offers=getAllOffersJSON()
    return offers

