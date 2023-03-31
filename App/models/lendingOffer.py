from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import date, datetime, timedelta

class LendingOffer(db.Model,UserMixin):
    __tablename__='lendingOffer'
    id = db.Column(db.Integer, primary_key=True)
    lenderID=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    itemDescription=db.Column(db.String(200), nullable=False)
    condition= db.Column(db.String(50), nullable=False)
    item= db.Column(db.String(200), nullable=False)
    category=db.Column(db.String(60), nullable=False)
    itemPic= db.Column(db.Text, nullable=True)
    itemPicName=db.Column(db.Text,nullable=True)
    #imageURL = db.Column(db.String(200))
    mimetype=db.Column(db.Text, nullable=True)
    preferedLocation= db.Column(db.String(100), nullable=False)
    Status= db.Column(db.String(50), nullable=False)
    RulesOfUse= db.Column(db.String(200), nullable=False)
    borrowDate=db.Column(db.Date, nullable=True)
    returnDate=db.Column(db.Date,nullable=True)
    
    lendRequests=db.relationship('LendingRequest',backref='lendingOffer',lazy="joined",cascade="all, delete-orphan")
    lendingnotif = db.relationship('LendingNotification',backref='lendingOffer',lazy=True,cascade="all, delete-orphan")
    interestedUserList=db.relationship('Manager',backref='lendingOffer',uselist=False)

    def __init__(self,lenderID,itemDescription,condition,item,category,itemPic,itemPicName,mimetype,preferedLocation,Status,RulesOfUse,borrowDate,returnDate):
        self.lenderID=lenderID
        self.itemDescription=itemDescription
        self.item=item
        self.category=category
        self.itemPic=itemPic
        self.itemPicName=itemPicName
        self.mimetype=mimetype
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
            'item': self.item,
            'lendingRequests':[lendRequest.toJSON() for lendRequest in self.lendRequests],
            'user': self.user,
            'itemDescription':self.itemDescription,
            'category':self.category,
            'condition': self.condition,
            #'itemPic':self.itemPic,
            #'itemPicName':self.itemPicName,
            'preferedLocation':self.preferedLocation,
            'Status':self.Status,
            'RulesOfUse':self.RulesOfUse,
            'borrowDate':self.borrowDate,
            'returnDate':self.returnDate
        }
    def toJSON2(self):
        return{
        'id': self.id,
        'lenderID':self.lenderID,
        'item': self.item,
        'user': self.user,
        'itemDescription':self.itemDescription,
        'category':self.category,
        'condition': self.condition,
        'itemPic':self.itemPic,
        'itemPicName':self.itemPicName,
        'mimetype':self.mimetype,
        'preferedLocation':self.preferedLocation,
        'Status':self.Status,
        'RulesOfUse':self.RulesOfUse,
        'borrowDate':self.borrowDate,
        'returnDate':self.returnDate
    }