from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager

from App.controllers import (
    create_lendingOffer, 
    get_offer_by_ID,
    get_lender,
    get_all_offers,
    update_Offer,
    remove_Offer
)

lendingOffer_views = Blueprint('lendingOffer_views', __name__, template_folder='../templates')

@lendingOffer_views.route('/createLendingOfferPage',methods=['POST'])
def makeOfferPage():
    data=request.form
    offer=create_lendingOffer(data['lenderID'],data['item'],data['condition'],data['preferedLocation'],data['Status'],data['rulesOfUse'])
    pass

@lendingOffer_views.route('/updateLendingOffer<OfferID>',methods=['POST'])
def changeOffer(OfferID):
    data=request.form
    offer=update_Offer(OfferID,data['item'],data['condition'],data['preferedLocation'],data['Status'],data['rulesOfUse'])
    pass

@lendingOffer_views.route('/removeLendingOffer<OfferID>',methods=['POST'])
def deleteOffer(OfferID):
    offer=remove_Offer(OfferID)
    pass
