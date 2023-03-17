from App.models import Manager,User
from App.database import db

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
        #obj=Manager(lendingoffer_ID=lendingoffer_ID,InterestedUserList=interestedUsers)
        db.session.add(interestedUsers)
        db.session.commit()
        return interestedUsers

def getList(lendingoffer_ID):
    data=Manager.query.filter_by(lendingOfferID=lendingoffer_ID).first()
    return data