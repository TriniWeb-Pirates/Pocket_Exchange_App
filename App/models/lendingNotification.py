from App.database import db
from flask_sqlalchemy import SQLAlchemy

class LendingNotification(db.Model):
    __tablename__='lendingNotification'
    notificationID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    requestID = db.Column(db.Integer, db.ForeignKey('lendingRequest.id'), nullable=False)
    itemID = db.Column(db.Integer, db.ForeignKey('lendingOffer.id'), nullable=False)
    notification = db.Column(db.String, nullable=False)

    def __init__(userID, requestID, itemID, notification):
        self.userID = userID
        self.requestID = requestID
        self.itemID = itemID
        self.notification = notification
    
    def toJSON(self):
        return{
            'notificationID':self.notificationID,
            'userID':self.userID,
            'requestID':self.requestID,
            'itemID': self.itemID,
            'notification':self.notification
        }

