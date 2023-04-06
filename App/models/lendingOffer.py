from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
#from App.models import LendingRequest
from datetime import date, datetime, timedelta

class LendingOffer(db.Model,UserMixin):
    __tablename__='lendingOffer'
    id = db.Column(db.Integer, primary_key=True)
    lenderID=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    borrowRequestID=db.Column(db.Integer, nullable=True)
    itemDescription=db.Column(db.String(200), nullable=False)
    condition= db.Column(db.String(50), nullable=False)
    item= db.Column(db.String(200), nullable=False)
    category=db.Column(db.String(60), nullable=False)
    imageURL = db.Column(db.String(200))
    preferedLocation= db.Column(db.String(100), nullable=False)
    Status= db.Column(db.String(50), nullable=False)
    RulesOfUse= db.Column(db.String(200), nullable=False)
    borrowDate=db.Column(db.Date, nullable=True)
    returnDate=db.Column(db.Date,nullable=True)
    
    lendRequests=db.relationship('LendingRequest',backref='lendingOffer',lazy="joined",cascade="all, delete-orphan")
    lendingnotif = db.relationship('LendingNotification',backref='lendingOffer',lazy=True,cascade="all, delete-orphan")
    interestedUserList=db.relationship('Manager',backref='lendingOffer',uselist=False)

    def __init__(self,lenderID,borrowRequestID,itemDescription,condition,item,category,imageURL,preferedLocation,Status,RulesOfUse,borrowDate,returnDate):
        self.lenderID=lenderID
        self.borrowRequestID=None
        self.itemDescription=itemDescription
        self.item=item
        self.category=category
        self.imageURL = imageURL
        self.condition=condition
        self.preferedLocation=preferedLocation
        self.Status=Status
        self.RulesOfUse=RulesOfUse
        self.borrowDate=borrowDate
        self.returnDate=returnDate
        

    def toJSON(self):
        return{
            'id': self.id,
            'lenderID':self.lenderID,
            'borrowRequestID':self.borrowRequestID,
            'item': self.item,
            'lendingRequests':[lendRequest.toJSON() for lendRequest in self.lendRequests],
            'user': self.user.toJSON(),
            'itemDescription':self.itemDescription,
            'category':self.category,
            'condition': self.condition,
            'imageURL':self.imageURL,
            'preferedLocation':self.preferedLocation,
            'Status':self.Status,
            'RulesOfUse':self.RulesOfUse,
            'borrowDate':self.borrowDate,
            'returnDate':self.returnDate
        }