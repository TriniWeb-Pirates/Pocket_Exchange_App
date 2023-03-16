from App.models import Manager,User
from App.database import db

def addToList(borrowerID,lendingoffer_ID):
    interestedUsers=Manager.query.filter_by(lendingoffer_ID).first()
    data=str(borrowerID)    
    interestedUsers.InterestedUserList=interestedUsers.InterestedUserList + "," + data
    return interestedUsers

def getList(lendingoffer_ID):
    data=Manager.query.filter_by(lendingOfferID=lendingoffer_ID).first()
    return data