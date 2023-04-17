from App.models import LendingOffer,LendingRequest,User,Manager
from App.database import db
from datetime import date, datetime, timedelta

#Function to create a lending offer
def create_lendingOffer(lenderID,item,category,itemDescription,imageURL,rulesOfUse,condition,preferedLocation):
    offer = LendingOffer(lenderID=lenderID,borrowRequestID=None, borrowingDays=None, item=item.lower(),category=category,itemDescription=itemDescription,imageURL=imageURL,RulesOfUse=rulesOfUse,condition=condition,preferedLocation=preferedLocation,Status="Available",returnDate=None,borrowDate=None,isReturned=False)
    db.session.add(offer)
    db.session.commit()
    return offer

#Function to set dates on a lending offer when the user has granted permanent approval of a request
def setDates(id,lendingRequestID,returnDate,borrowDate):
    offer=LendingOffer.query.get(id)
    request=LendingRequest.query.get(lendingRequestID)
    if(request.tempApproval==True):
        offer.returnDate=datetime.date(datetime.strptime(returnDate, "%Y-%m-%d"))
        offer.borrowDate=datetime.date(datetime.strptime(borrowDate, "%Y-%m-%d"))
        db.session.add(offer)
        db.session.commit()
        days = findBorrowingDays(offer.id)
        return offer
    else:
        return "Action Denied, this lending request must be temporarily approved first"

#Function to search for a lending offer and return a list of dicts 
def findItems(userInput):
    data=userInput.lower()
    results=LendingOffer.query.filter_by(item=data).all()
    findings = [result.toJSON() for result in results]
    return findings

#Function to return a list of dicts for all offers
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

#Function to return number of days an item has borrowed for
def findBorrowingDays(offerID):
    offer=LendingOffer.query.get(offerID)
    today=date.today()
    if(offer.borrowDate!=None and offer.returnDate!=None):
        if(today>=offer.borrowDate):
            borrowingDays=offer.returnDate-today
            offer.borrowingDays = borrowingDays.days
            db.session.add(offer)
            db.session.commit()
            return borrowingDays
        else:
            borrowingDays=offer.returnDate-offer.borrowDate
            offer.borrowingDays = borrowingDays.days
            db.session.add(offer)
            db.session.commit()
            return borrowingDays
    
    else:
        return None
    


# updates the borrowing days in the database
def getAllBorrowingDays():
    offers = LendingOffer.query.all()
    for offer in offers:
        findBorrowingDays(offer.id)
    return offers

#Function to check the status of the offer and return a message whether the item is late or still has time before returned
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

#Function to remove a lending offer
def remove_Offer(id):
    offer=get_offer_by_ID(id)
    manager_for_offer=Manager.query.filter_by(lendingOfferID=offer.id).first()
    if(manager_for_offer):
        db.session.delete(manager_for_offer)
        db.session.commit()    
    db.session.delete(offer)
    db.session.commit()
    return offer

#Function to return a list of dicts for all items in a category
def getItmesByCategory(category):
    data=LendingOffer.query.filter_by(category=category).all()
    items = [offer.toJSON() for offer in data]
    return items

#Function to return all user offers in a list of dicts 
def getAllUserOffers(userID):
    offers=LendingOffer.query.filter_by(lenderID=userID).all()
    items = [offer.toJSON() for offer in offers]
    return items

#Function to restart offer and reset data in the offer and remove associated requests
def restartOffer(userID,id):
    offer=LendingOffer.query.get(id)
    if(userID==offer.lenderID):
        for request in offer.lendRequests:
            item=LendingRequest.query.get(request.id)
            db.session.delete(item)
            db.session.commit()
        offer.borrowRequestID=None
        offer.borrowingDays=None
        offer.returnDate = None
        offer.borrowDate = None
        offer.isReturned = False
        offer.Status="Available"
        manager = Manager.query.filter_by(lendingOfferID=offer.id).first()
        manager.InterestedUserList = ''
        db.session.add(manager)
        db.session.commit()
        db.session.add(offer)
        db.session.commit()
        return offer.toJSON()
    else:
        return "Action denied, You cannit restart this offer"


#Function to return approved request for an offer
def getApprovedRequest(offers):
    for offer in offers:
        offer = LendingOffer.query.get(lendingOfferID)
        if(offer.borrowRequestID!=None):
            approvedRequest = LendingRequest.query.get(offer.borrowRequestID)
            return approvedRequest
        else:
            return None

#Function to return the return date on a lending offer
def getReturnDate(lendingoffer_ID):
    offer = LendingOffer.query.get(lendingoffer_ID)
    if(offer.returnDate):
        return offer.returnDate
    else:
        return None

#Function to set the isReturned to true
def changeIsReturned(id,userID):
    lendingOffer=LendingOffer.query.get(id)
    lendingRequest = LendingRequest.query.get(lendingOffer.borrowRequestID)
    #if(lendingRequest.tempApproval==True and lendingRequest.Status==True and lendingRequest.borrowerID!=userID):
    if(lendingRequest.tempApproval==True  and lendingRequest.borrowerID!=userID):
        lendingOffer.isReturned=True
        lendingOffer.Status="Unavailable"
        db.session.add(lendingOffer)
        db.session.commit()
        return lendingOffer.toJSON()

    return "Action Denied, User must grant temporary approval to the lending request before changing the status of it"


