from App.models import LendingRequest
from App.database import db
from datetime import datetime

def create_lendingRequest(lenderID,lendingoffer_ID,preferedLocation ,Status,quantity,tempApproval,borrowingDays,returnDate,borrowDate):
    returnDate=datetime.date(datetime.strptime(returnDate, "%Y-%m-%d"))
    borrowDate=datetime.date(datetime.strptime(borrowDate, "%Y-%m-%d"))
    request = LendingRequest(lenderID=lenderID,lendingoffer_ID=lendingoffer_ID,preferedLocation=preferedLocation,Status=Status,quantity=quantity,tempApproval=tempApproval,borrowingDays=borrowingDays,returnDate=returnDate,borrowDate=borrowDate)
    db.session.add(request)
    db.session.commit()
    return request

def getAllRequestsJSON():
    data = LendingRequest.query.all()
    if not data:
        return []
    items = [request.toJSON() for request in data]
    return items

def get_request_by_ID(id):
    return LendingRequest.query.filter_by(id=id).first()
    
def calculateBorrowingDays(borrowDate,returnDate):
    #code to calculate days
    pass


def updateLendingRequest(id,lenderID,lendingoffer_ID,preferedLocation ,Status,quantity,tempApproval,borrowingDays, borrowDate,returnDate):
    request=get_request_by_ID(id)
    request.preferedLocation=preferedLocation
    request.Status=Status
    request.quantity=quantity
    request.tempApproval=tempApproval
    #request.borrowingDays=calculateBorrowingDays(borrowDate,returnDate)
    request.borrowingDays=3
    request.borrowDate=borrowDate
    request.returnDate=returnDate
    return request

def countRequests(lenderID):
    requests=LendingRequest.query.filter_by(lenderID=lenderID).all()
    items = [request.toJSON() for request in requests]
    count=0
    for item in items:
        count=count+1
    if count>=3:
        return "Maximum Lending Request Limit Reached, User Can Only Have 3 Active Lending Requests"
    return None