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

def update_Offer(OfferID,item,condition,preferedLocation,Status,rulesOfUse):
    offer=LendingOffer.query.get(OfferID)
    offer.item=item
    offer.condition=condition
    offer.preferedLocation=preferedLocation
    offer.Status=Status
    offer.RulesOfUse=rulesOfUse
    db.session.add(offer)
    db.session.commit()
    return offer

def remove_Offer(id):
    offer=LendingOffer.query.get(id)
    db.session.delete(offer)
    db.session.commit()
    return offer
