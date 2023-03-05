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

def get_request_by_ID(id):
    return LendingRequest.query.filter_by(id=id).first()