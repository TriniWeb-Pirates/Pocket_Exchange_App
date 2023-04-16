from App.models import LendingNotification,LendingOffer,LendingRequest
from App.database import db

#String variable used to create the lending notification
message=" is unavailable at this time, Please try again when it is made available "

#Function to create a lending notification to users who did not get their item approved
def createNotification(userID,itemID,message):
    userNotification=LendingNotification(userID=userID, itemID=itemID, notification=message)
    db.session.add(userNotification)
    db.session.commit()
    return userNotification

#Function to send lending notifications to other users 
def notifyUsers(subscriberList,lendingoffer_ID):
    offer=LendingOffer.query.get(lendingoffer_ID)
    request = LendingRequest.query.get(offer.borrowRequestID)
    approvedUser = request.borrowerID
    user = str(approvedUser)
    name=str(offer.item)
    fullMessage=name+message
    for value in subscriberList:
        if(value!=','):
            if(value!=user):
                user=int(value) 
                notification=createNotification(user,lendingoffer_ID,fullMessage)
            else:
                notification= None
    return notification

#Function to return all lending notifications in a list of dicts
def getAllNotifications():
    items=LendingNotification.query.all()
    data = [item.toJSON() for item in items]
    return data

#Function to return all lending notifications of a user in a list of dicts
def getAllUserLendingNotifications(userID):
    messages=LendingNotification.query.filter_by(userID=userID).all()
    if(messages):
        notifications = [message.toJSON() for message in messages]
        return notifications
    else:
        return "You currently have no Lending Notifications"


#Function to delete a lending notification
def deleteNotification(notificationID):
    notification = LendingNotification.query.get(notificationID)
    print(notification)
    db.session.delete(notification)
    db.session.commit()
    return 'Notification deleted.'