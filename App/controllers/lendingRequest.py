from App.models import LendingRequest
from App.database import db

def create_lendingRequest(lenderID,offerID,preferedLocation ,Status,quantity,tempApproval,borrowingDays,returnDate,borrowDate):
    request = LendingRequest(lenderID=lenderID,offerID=offerID,preferedLocation=preferedLocation,Status=Status,quantity=quantity,tempApproval=tempApproval,borrowingDays=borrowingDays,returnDate=returnDate,borrowDate=borrowDate)
    db.session.add(request)
    db.session.commit()
    return request

def get_request_by_ID(id):
    return LendingRequest.query.filter_by(id=id).first()