from App.models import LendingOffer,LendingRequest,User
from App.database import db
from datetime import datetime

def create_lendingOffer(lenderID,item,category,itemDescription,imageURL,rulesOfUse,condition,preferedLocation):
    offer = LendingOffer(lenderID=lenderID,borrowRequestID=None,item=item.lower(),category=category,itemDescription=itemDescription,imageURL=imageURL,RulesOfUse=rulesOfUse,condition=condition,preferedLocation=preferedLocation,Status="Available",returnDate=None,borrowDate=None)
    db.session.add(offer)
    db.session.commit()
    return offer

def setDates(id,lendingRequestID,returnDate,borrowDate):
    offer=LendingOffer.query.get(id)
    request=LendingRequest.query.get(lendingRequestID)
    if(request.tempApproval==True):
        offer.returnDate=datetime.date(datetime.strptime(returnDate, "%Y-%m-%d"))
        offer.borrowDate=datetime.date(datetime.strptime(borrowDate, "%Y-%m-%d"))
        return offer
    else:
        return "Action Denied, this lending request must be temporarily approved first"

def findItems(userInput):
    data=userInput.lower()
    results=LendingOffer.query.filter_by(item=data).all()
    findings = [result.toJSON() for result in results]
    print(findings)
    return findings


def getAllOffersJSON():
    data = LendingOffer.query.all()
    if not data:
        return []
    items = [offer.toJSON() for offer in data]
    #print(items)
    return items

def get_offer_by_ID(id):
    return LendingOffer.query.filter_by(id=id).first()

def get_lender(lenderID):
    return User.query.get(lenderID)

def get_all_offers():
    return LendingOffer.query.all()


def update_Offer(OfferID,item,itemDescription,category,imageURL,condition,preferedLocation,rulesOfUse):
    offer=LendingOffer.query.get(OfferID)
    offer.item=item
    offer.itemDescription=itemDescription
    offer.category=category
    offer.condition=condition
    offer.imageURL = imageURL
    offer.preferedLocation=preferedLocation
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

def getAllUserOffers(userID):
    offers=LendingOffer.query.filter_by(lenderID=userID).all()
    items = [offer.toJSON() for offer in offers]
    return items

def restartOffer(userID,id):
    offer=LendingOffer.query.get(id)
   # print(offer.toJSON())
    if(userID==offer.lenderID):
        for request in offer.lendRequests:
           #print("HERE")
            item=LendingRequest.query.get(request.id)
            #print(item)
            db.session.delete(item)
            db.session.commit()
        offer.borrowRequestID=None
        offer.Status="Available"
        db.session.add(offer)
        db.session.commit()
        #print(offer)
        return offer.toJSON()
    else:
        return "Action denied, You cannit restart this offer"