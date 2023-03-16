from App.models import LendingNotification,User
from App.database import db

message="Sorry but the item you have requested is unavailable at this time, Please try again when it is made available "

def createNotification(userID,requestID,itemID):
    userNotification=LendingNotification(userID=userID,requestID=requestID, itemID=itemID, notification=message)
    db.session.add(userNotification)
    db.session.commit()
    return userNotification

def notifyUsers(subscriberList):
    for value in subscriberList:
        if(value!=','):
            user=int(value)
            pass
            #notification=createNotification(user)
