from App.models import LendingOffer,User
from App.database import db

def create_lendingOffer(lenderID,item,condition,preferedLocation,Status,rulesOfUse):
    offer = LendingOffer(lenderID=lenderID,item=item,condition=condition,preferedLocation=preferedLocation,Status=Status,RulesOfUse=rulesOfUse)
    db.session.add(offer)
    db.session.commit()
    return offer

def get_offer_by_ID(OfferID):
    return LendingOffer.query.filter_by(OfferID=OfferID).first()

def get_lender(lenderID):
    return User.query.get(lenderID)

def get_all_offers():
    return LendingOffer.query.all()