from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime

class Message(db.Model):
    messageId = db.Column(db.Integer, primary_key=True)
    lenderID =  db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    recieverID =  db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(1000), nullable=False)
    timeSent=db.Column(db.datetime,nullable=False)

    def __init__(self,lenderID,recieverID ,message, timeSent):
        self.lenderID=lenderID
        self.recieverID=recieverID
        self.message = message
        self.timeSent=timeSent
        

    def toJSON(self):
        return{
            'messageID': self.messageID,
            'lenderID':self.lenderID,
            'recieverID': self.recieverID,
            'message': self.message,
            'timeSent': self.timeSent
            
        }