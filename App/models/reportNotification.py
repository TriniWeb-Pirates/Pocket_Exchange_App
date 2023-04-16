from App.database import db
from flask_sqlalchemy import SQLAlchemy

class ReportNotification(db.Model):
    __tablename__='reportNotification'
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    notification = db.Column(db.String(200), nullable=False)

    def __init__(self,userID, notification):
        self.userID = userID
        self.notification = notification
    
    def toJSON(self):
        return{
            'id':self.id,
            'userID':self.userID,
            'notification':self.notification
        }

