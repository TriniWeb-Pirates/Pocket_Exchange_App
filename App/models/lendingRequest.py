from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime, timedelta
from App.models import LendingOffer
from flask_login import UserMixin


class LendingRequest(db.Model,UserMixin):
    __tablename__='lendingRequest'
    id = db.Column(db.Integer, primary_key=True)
    lenderID =  db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    lendingoffer_ID= db.Column(db.Integer,db.ForeignKey('lendingOffer.id'), nullable=False)
    preferedLocation= db.Column(db.String(100), nullable=False)
    Status= db.Column(db.Boolean,nullable=False)
    quantity= db.Column(db.Integer,nullable=False)
    tempApproval=db.Column(db.Boolean,nullable=False)
    borrowingDays= db.Column(db.Integer, nullable=False)
    returnDate=db.Column(db.Date,nullable=False)
    borrowDate=db.Column(db.Date, nullable=False)
    lendingnotif=db.relationship('LendingNotification',backref='lendingRequest',lazy=True,cascade="all, delete-orphan")
    
    

    def __init__(self,lenderID, lendingoffer_ID,preferedLocation,Status,quantity,tempApproval ,borrowingDays, returnDate,borrowDate):
        self.lenderID=lenderID
        self.lendingoffer_ID=lendingoffer_ID
        self.preferedLocation=preferedLocation
        self.Status=Status
        self.quantity=quantity
        self.tempApproval=tempApproval
        self.borrowingDays=borrowingDays
        self.returnDate=returnDate
        self.borrowDate=borrowDate
        
        

    def toJSON(self):
        return{
            'lendRequestID': self.lendRequestID,
            'lendingoffer_ID': self.lendingoffer_ID,
            'preferedLocation': self.preferedLocation,
            'Status': self.Status,
            'quantity': self.quantity,
            'tempApproval': self.tempApproval,
            'lenderID': self.lenderID,
            'borrowingDays':self.borrowingDays,
            'returnDate': self.returnDate,
            'borrowDate': self.borrowDate
            
        }