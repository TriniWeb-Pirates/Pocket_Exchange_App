from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime


class LendingRequest(db.Model):
    lendRequestID = db.Column(db.Integer, primary_key=True)
    lenderID =  db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    borrowingDays= db.Column(db.Integer, nullable=False)
    returnDate=db.Column(db.datetime,nullable=False)
    borrowDate=db.Column(db.datatime, nullable=False)
    

    def __init__(self,lenderID ,borrowingDays, returnDate,borrowDate):
        self.lenderID=lenderID
        self.borrowingDays=borrowingDays
        self.returnDate=returnDate
        self.borrowDate=borrowDate
        
        

    def toJSON(self):
        return{
            'lendRequestID': self.lendRequestID,
            'lenderID': self.lenderID,
            'borrowingDays':self.borrowingDays,
            'returnDate': self.returnDate,
            'borrowDate': self.borrowDate
            
        }