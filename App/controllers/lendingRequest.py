from App.models import LendingRequest, LendingOffer,User, Manager
from App.database import db
from datetime import datetime

#Function to create a lending request
def create_lendingRequest(borrowerID,lendingoffer_ID,reasonForUse,preferedLocation):
    response=countRequests(borrowerID)
    if(response):
        return response
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

    if(data==None):
        request = LendingRequest(borrowerID=borrowerID,lendingoffer_ID=lendingoffer_ID,reasonForUse=reasonForUse,preferedLocation=preferedLocation,Status=False,tempApproval=False)
        db.session.add(request)
        db.session.commit()
        return "Borrow request created successfully. You can see the status of your request in the My Items Page > My Borrow Requests. "
    else:
        return "Request denied, user can not request their own lending offer"

def create_lendingRequest_for_testing(borrowerID,lendingoffer_ID,reasonForUse,preferedLocation):
    response=countRequests(borrowerID)
    if(response):
        return response
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

    if(data==None):
        request = LendingRequest(borrowerID=borrowerID,lendingoffer_ID=lendingoffer_ID,reasonForUse=reasonForUse,preferedLocation=preferedLocation,Status=False,tempApproval=False)
        db.session.add(request)
        db.session.commit()
        return request.toJSON()
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

#function to return all user requests in a list of dicts
def getAllUserRequestsJSON(borrowerID):
    data = LendingRequest.query.filter_by(borrowerID=borrowerID).all()
    print(data)
    if not data:
        return []
    items = [request.toJSON() for request in data]
    return items

def get_request_by_ID(id):
    return LendingRequest.query.filter_by(id=id).first()
    
def updateLendingRequest(id,borrowerID,lendingoffer_ID,reasonForUse,preferedLocation):
    request=get_request_by_ID(id)
    request.reasonForUse=reasonForUse
    request.preferedLocation=preferedLocation
    return request

#Function to count lending requests for an offer
def countRequests(borrowerID):
    requests=LendingRequest.query.filter_by(borrowerID=borrowerID).all()
    items = [request.toJSON() for request in requests]
    count=0
    for item in items:
        count=count+1
    if count>=3:
        return "Maximum Borrow Request Limit Reached, User Can Only Have 3 Active Borrow Requests"
    return None

def getAllOfferRequests(lendingoffer_ID):
    requests=LendingRequest.query.filter_by(lendingoffer_ID=lendingoffer_ID).all()
    items = [request.toJSON() for request in requests]
    return items

#Function to grant temp approval for a lending request
def grantTempApproval(id,lendingoffer_ID,userID):
    request=LendingRequest.query.get(id)
    offer=LendingOffer.query.get(lendingoffer_ID)
    if(request.borrowerID!=userID):
        request.tempApproval=True
        db.session.add(request)
        db.session.commit()
        offer.borrowRequestID=id
        offer.Status="Unavailable"
        db.session.add(offer)
        db.session.commit()
        print(request.toJSON())
        return request.toJSON()
    else:
        #return "Approval denied, users can not approve their own lending requests"
        return None

#Function to unapprove a lending request
def UnapproveTemp(id,userID):
    request=LendingRequest.query.get(id)
    offer=LendingOffer.query.filter_by(id=request.lendingoffer_ID,lenderID=userID).first()
    if(userID!=request.borrowerID and offer.lenderID==userID):
        request.tempApproval=False
        offer.borrowRequestID=None
        offer.Status="Available"
        db.session.add(request)
        db.session.commit()
        db.session.add(offer)
        db.session.commit()
        return request.toJSON()
    else:
        return "Action Denied"

#Function to set the status of a request to true and set the associated offer status to Unavailable
def changeStatus(id,userID):
    lendingRequest=LendingRequest.query.get(id)
    if(lendingRequest.tempApproval==True and lendingRequest.borrowerID!=userID):
        lendingRequest.Status=True
        offer=LendingOffer.query.get(lendingRequest.lendingoffer_ID)
        offer.Status="Unavailable"
        db.session.add(lendingRequest)
        db.session.commit()
        db.session.add(offer)
        db.session.commit()
        return lendingRequest.toJSON()
    return "Action Denied, User must grant temporary approval to the lending request before changing the status of it"


#Function to delete a lending request and update the manager object for the associated lending offer
def deleteLendingRequest(requestID):

    request = LendingRequest.query.get(requestID)
    offer = LendingOffer.query.get(request.lendingoffer_ID)

    if(request.tempApproval==True):
        offer.borrowRequestID=None
        offer.Status = "Available"

    if(request.Status==True):
        offer.borrowingDays=None
        offer.returnDate = None
        offer.startDate = None

    if(offer.isReturned==True):
        offer.isReturned=False

    manager=Manager.query.filter_by(lendingOfferID=request.lendingoffer_ID).first()
    x=request.borrowerID
    person=str(x)
    if(manager!=None):
        for value in manager.InterestedUserList:
            
            if(value==person):
                manager.InterestedUserList=manager.InterestedUserList.replace(value,",")
                db.session.add(manager)
                db.session.commit()

    db.session.add(offer)
    db.session.commit()

    db.session.delete(request)
    db.session.commit()

    return 'Request was successfully deleted'





         