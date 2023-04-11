from App.models import LendingNotification,LendingOffer,LendingRequest
from App.database import db

message=" is unavailable at this time, Please try again when it is made available "

#def createNotification(userID,requestID,itemID):
def createNotification(userID,itemID,message):
    #userNotification=LendingNotification(userID=userID,requestID=requestID, itemID=itemID, notification=message)
    userNotification=LendingNotification(userID=userID, itemID=itemID, notification=message)
    db.session.add(userNotification)
    db.session.commit()
    return userNotification

def notifyUsers(subscriberList,lendingoffer_ID):
    offer=LendingOffer.query.get(lendingoffer_ID)
    request = LendingRequest.query.get(offer.borrowRequestID)
    approvedUser = request.borrowerID
    user = str(approvedUser)

    name=str(offer.item)
    fullMessage=name+message
    for value in subscriberList:
        if(value!=',' and str(value)!=user):
            print('the value of value right now is')
            print(value)
            user=int(value)
            notification=createNotification(user,lendingoffer_ID,fullMessage)
            print(notification)
    return notification

def getAllNotifications():
    items=LendingNotification.query.all()
    data = [item.toJSON() for item in items]
    return data

def getAllUserLendingNotifications(userID):
    messages=LendingNotification.query.filter_by(userID=userID).all()
    if(messages):
        notifications = [message.toJSON() for message in messages]
        return notifications
    else:
        return "You currently have no Lending Notifications"



def deleteNotification(notificationID):
    notification = LendingNotification.query.get(notificationID)
    print(notification)
    db.session.delete(notification)
    db.session.commit()
    
    return 'Notification deleted.'