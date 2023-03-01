from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime
from App.models import Request


class LendingRequest(db.Model,Request):
    lendRequestID = db.Column(db.Integer, primary_key=True)
    lenderID =  db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    offerID= db.Column(db.Integer,db.ForeignKey('lendingOffer.id'), nullable=False)
    item= db.Column(db.String(200),nullable=False)
    Status= db.Column(db.Boolean,nullable=False)
    quantity= db.Column(db.Integer,nullable=False)
    tempApproval=db.Column(db.Boolean,nullable=False)
    borrowingDays= db.Column(db.Integer, nullable=False)
    returnDate=db.Column(db.datetime,nullable=False)
    borrowDate=db.Column(db.datatime, nullable=False)
    
    

    def __init__(self,lenderID, offerID,item,Status,quantity,tempApproval ,borrowingDays, returnDate,borrowDate):
        self.lenderID=lenderID
        self.offerID=offerID
        self.item=item
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
            'item': self.item,
            'Status': self.Status,
            'quantity': self.quantity,
            'tempApproval': self.tempApproval,
            'lenderID': self.lenderID,
            'borrowingDays':self.borrowingDays,
            'returnDate': self.returnDate,
            'borrowDate': self.borrowDate
            
        }