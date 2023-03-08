from App.models import LendingOffer,User
from App.database import db

def create_lendingOffer(lenderID,item,category,condition,preferedLocation,Status,rulesOfUse):
    offer = LendingOffer(lenderID=lenderID,item=item,category=category,condition=condition,preferedLocation=preferedLocation,Status=Status,RulesOfUse=rulesOfUse)
    db.session.add(offer)
    db.session.commit()
    return offer

def getAllOffersJSON():
    data = LendingOffer.query.all()
    if not data:
        return []
    items = [offer.toJSON() for offer in data]
    return items

def get_offer_by_ID(id):
    return LendingOffer.query.filter_by(id=id).first()

def get_lender(lenderID):
    return User.query.get(lenderID)

def get_all_offers():
    return LendingOffer.query.all()

def update_Offer(OfferID,item,category,condition,preferedLocation,Status,rulesOfUse):
    offer=LendingOffer.query.get(OfferID)
    offer.item=item
    offer.category=category
    offer.condition=condition
    offer.preferedLocation=preferedLocation
    offer.Status=Status
    offer.RulesOfUse=rulesOfUse
    db.session.add(offer)
    db.session.commit()
    return offer

def remove_Offer(id):
   # offer=LendingOffer.query.get(id)
    offer=get_offer_by_ID(id)
    db.session.delete(offer)
    db.session.commit()
    return offer

def getItmesByCategory(category):
    data=LendingOffer.query.filter_by(category=category).all()
    items = [offer.toJSON() for offer in data]
    return items

