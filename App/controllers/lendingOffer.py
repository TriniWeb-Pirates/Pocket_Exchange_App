from App.models import LendingOffer,LendingRequest,User,Manager
from App.database import db
from datetime import date, datetime, timedelta

def create_lendingOffer(lenderID,item,category,itemDescription,imageURL,rulesOfUse,condition,preferedLocation):
    offer = LendingOffer(lenderID=lenderID,borrowRequestID=None, borrowingDays=None, item=item.lower(),category=category,itemDescription=itemDescription,imageURL=imageURL,RulesOfUse=rulesOfUse,condition=condition,preferedLocation=preferedLocation,Status="Available",returnDate=None,borrowDate=None,isReturned=False)
    db.session.add(offer)
    db.session.commit()
    return offer

def setDates(id,lendingRequestID,returnDate,borrowDate):
    offer=LendingOffer.query.get(id)
    request=LendingRequest.query.get(lendingRequestID)
    if(request.tempApproval==True):
        offer.returnDate=datetime.date(datetime.strptime(returnDate, "%Y-%m-%d"))
        offer.borrowDate=datetime.date(datetime.strptime(borrowDate, "%Y-%m-%d"))
        print(offer.returnDate)
        print(offer.borrowDate)
        db.session.add(offer)
        db.session.commit()
        days = findBorrowingDays(offer.id)
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

def findBorrowingDays(offerID):
    offer=LendingOffer.query.get(offerID)
    today=date.today()
    if(offer.borrowDate!=None and offer.returnDate!=None):
        if(today>=offer.borrowDate):
            borrowingDays=offer.returnDate-today
            print(borrowingDays.days)
            offer.borrowingDays = borrowingDays.days
            db.session.add(offer)
            db.session.commit()
            
            return borrowingDays
        else:
            borrowingDays=offer.returnDate-offer.borrowDate
            offer.borrowingDays = borrowingDays.days
            db.session.add(offer)
            db.session.commit()
            print(borrowingDays)
            return borrowingDays
    
    else:
        return None
    


# updates the borrowing days in the database
def getAllBorrowingDays():
    offers = LendingOffer.query.all()
    for offer in offers:
        findBorrowingDays(offer.id)
    return offers

def checkDate(offerID):
    offer=LendingOffer.query.get(offerID)
    today=datetime.date.today()
    if(offer.returnDate<today):
        return "The user who borrowed this item is late"
    else:
        days=findBorrowingDays(offerID)
        return "The borrower has "+ str(days)+ "to return this item"



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
    manager_for_offer=Manager.query.filter_by(lendingOfferID=offer.id).first()
    if(manager_for_offer):
        db.session.delete(manager_for_offer)
        db.session.commit()    
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
        offer.borrowingDays=None
        offer.returnDate = None
        offer.borrowDate = None
        offer.isReturned = False
        offer.Status="Available"
        db.session.add(offer)
        db.session.commit()
        print(offer.toJSON())
        return offer.toJSON()
    else:
        return "Action denied, You cannit restart this offer"



def getApprovedRequest(offers):
    for offer in offers:
        offer = LendingOffer.query.get(lendingOfferID)
        if(offer.borrowRequestID!=None):
            approvedRequest = LendingRequest.query.get(offer.borrowRequestID)
            return approvedRequest
        else:
            return None


def getReturnDate(lendingoffer_ID):
    offer = LendingOffer.query.get(lendingoffer_ID)
    if(offer.returnDate):
        return offer.returnDate
    else:
        return None
    
def changeIsReturned(id,userID):
    lendingOffer=LendingOffer.query.get(id)
    lendingRequest = LendingRequest.query.get(lendingOffer.borrowRequestID)

    if(lendingRequest.tempApproval==True and lendingRequest.Status==True and lendingRequest.borrowerID!=userID):
        lendingOffer.isReturned=True
        lendingOffer.Status="Unavailable"
        db.session.add(lendingOffer)
        db.session.commit()
        return lendingOffer.toJSON()

    return "Action Denied, User must grant temporary approval to the lending request before changing the status of it"


