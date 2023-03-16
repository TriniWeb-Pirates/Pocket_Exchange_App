from App.models import LendingNotification,User
from App.database import db

message="Sorry but the item you have requested is unavailable at this time, Please try again when it is made available "

def createNotification(userID,requestID,itemID):
    userNotification=LendingNotification(userID=userID,requestID=requestID, itemID=itemID, notification=message)
    db.session.add(userNotification)
    db.session.commit()
    return userNotification

def notifyUsers(subscriberList):
    for user in subscriberList:
        if(user!=','):
            user=int(user)
    pass