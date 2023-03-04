from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from datetime import date, datetime, timedelta
from App.models import LendingOffer


class LendingRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lenderID =  db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    offerID= db.Column(db.Integer,db.ForeignKey(LendingOffer.id), nullable=False)
    preferedLocation= db.Column(db.String(100), nullable=False)
    Status= db.Column(db.Boolean,nullable=False)
    quantity= db.Column(db.Integer,nullable=False)
    tempApproval=db.Column(db.Boolean,nullable=False)
    borrowingDays= db.Column(db.Integer, nullable=False)
    returnDate=db.Column(db.Date,nullable=False)
    borrowDate=db.Column(db.Date, nullable=False)
    lendingnotif=db.relationship('LendingNotification',backref='lendingRequest',lazy=True,cascade="all, delete-orphan")
    
    

    def __init__(self,lenderID, offerID,preferedLocation,Status,quantity,tempApproval ,borrowingDays, returnDate,borrowDate):
        self.lenderID=lenderID
        self.offerID=offerID
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
            'offerID': self.offerID,
            'preferedLocation': self.preferedLocation,
            'Status': self.Status,
            'quantity': self.quantity,
            'tempApproval': self.tempApproval,
            'lenderID': self.lenderID,
            'borrowingDays':self.borrowingDays,
            'returnDate': self.returnDate,
            'borrowDate': self.borrowDate
            
        }