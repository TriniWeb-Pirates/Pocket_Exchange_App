from App.models import LendingRequest, LendingOffer,User
from App.database import db
from datetime import datetime

def create_lendingRequest(borrowerID,lendingoffer_ID,reasonForUse,preferedLocation):
    #returnDate=datetime.date(datetime.strptime(returnDate, "%Y-%m-%d"))
    #borrowDate=datetime.date(datetime.strptime(borrowDate, "%Y-%m-%d"))
    validUser=User.query.get(borrowerID)
    if(validUser==None):
        return "Request denied, user does not exist"
    validOffer=LendingOffer.query.get(lendingoffer_ID)
    if(validOffer==None):
        return "Request denied, lending offer does not exist"
    data=LendingOffer.query.filter_by(id=lendingoffer_ID,lenderID=borrowerID).first()
    duplicate = LendingRequest.query.filter_by(lendingoffer_ID=lendingoffer_ID, borrowerID=borrowerID).first()
    if(duplicate):
        return "Request denied, you cannot make more than one request per item. "

    #data=LendingOffer.query.get(lendingoffer_ID)
    if(data==None):
        request = LendingRequest(borrowerID=borrowerID,lendingoffer_ID=lendingoffer_ID,reasonForUse=reasonForUse,preferedLocation=preferedLocation,Status=False,tempApproval=False,isReturned=False)
        db.session.add(request)
        db.session.commit()
        return "Lending request created"
    else:
        return "Request denied, user can not request their own lending offer"

def getAllRequestsJSON():
    data = LendingRequest.query.all()
    if not data:
        return []
    items = [request.toJSON() for request in data]
    return items

def getRequest(id):
    request=LendingRequest.query.get(id)
    return request.toJSON()

def getAllUserRequestsJSON(borrowerID):
    data = LendingRequest.query.filter_by(borrowerID=borrowerID).all()
    if not data:
        return []
    items = [request.toJSON() for request in data]
    return items

def get_request_by_ID(id):
    return LendingRequest.query.filter_by(id=id).first()
    
def calculateBorrowingDays(borrowDate,returnDate):
    #code to calculate days
    pass


def updateLendingRequest(id,borrowerID,lendingoffer_ID,reasonForUse,preferedLocation):
    request=get_request_by_ID(id)
    request.reasonForUse=reasonForUse
    request.preferedLocation=preferedLocation
    return request

def countRequests(borrowerID):
    requests=LendingRequest.query.filter_by(borrowerID=borrowerID).all()
    items = [request.toJSON() for request in requests]
    count=0
    for item in items:
        count=count+1
    if count>=3:
        return "Maximum Lending Request Limit Reached, User Can Only Have 3 Active Lending Requests"
    return None

def getAllOfferRequests(lendingoffer_ID):
    requests=LendingRequest.query.filter_by(lendingoffer_ID=lendingoffer_ID).all()
    items = [request.toJSON() for request in requests]
    return items

#grantApproval must be revised
def grantTempApproval(id,lendingoffer_ID,userID,status):
    request=LendingRequest.query.get(id)
    offer=LendingOffer.query.get(lendingoffer_ID)
    if(request.borrowerID!=userID):
        request.tempApproval=status
        db.session.add(request)
        db.session.commit()
        offer.borrowRequestID=int(id)
        offer.Status="Unavailable"
        #print(offer.toJSON())
        #return "Approval Granted"
        return request.toJSON()
    else:
        return "Approval denied, users can not approve their own lending requests"

def UnapproveTemp(id,userID):
    request=LendingRequest.query.get(id)
    offer=LendingOffer.query.filter_by(id=request.lendingoffer_ID,lenderID=userID).first()
    if(userID!=request.borrowerID and offer.lenderID==userID):
        request.tempApproval=False
        offer.Status=None
        print(offer.toJSON())
        return request 


def changeStatus(id,userID,status):
    lendingRequest=LendingRequest.query.get(id)
    
    if(lendingRequest.tempApproval==True and lendingRequest.borrowerID!=userID):
        lendingRequest.Status=status
        offer=LendingOffer.query.get(lendingRequest.lendingoffer_ID)
        offer.Status=status
        return lendingRequest.toJSON()
    return "Action Denied, User must grant temporary approval to the lending request before changing the status of it"

def changeIsReturned(id,userID,isReturned):
    lendingRequest=LendingRequest.query.get(id)
    if(lendingRequest.tempApproval==True and lendingRequest.Status==True and lendingRequest.borrowerID!=userID):
        lendingRequest.isReturned=isReturned
        offer=LendingOffer.query.get(lendingRequest.lendingoffer_ID)
        offer.Status=False
        return lendingRequest.toJSON()
    return "Action Denied, User must grant temporary approval to the lending request before changing the status of it"