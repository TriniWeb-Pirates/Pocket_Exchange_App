from App.models import Manager,User
from App.database import db

#Function to add users to the subscriber list for a lending offer
def addToList(borrowerID,lendingoffer_ID):
    interestedUsers=Manager.query.filter_by(lendingOfferID=lendingoffer_ID).first()
    if(interestedUsers==None):
        data=str(borrowerID)
        obj=Manager(lendingOfferID=lendingoffer_ID,InterestedUserList=data)
        db.session.add(obj)
        db.session.commit()    
        return obj
    else:
        data=str(borrowerID)
        interestedUsers.InterestedUserList=interestedUsers.InterestedUserList + "," + data
        db.session.add(interestedUsers)
        db.session.commit()
        return interestedUsers

#Function to get the manager object for a lending offer
def getList(lendingoffer_ID):
    data=Manager.query.filter_by(lendingOfferID=lendingoffer_ID).first()
    return data