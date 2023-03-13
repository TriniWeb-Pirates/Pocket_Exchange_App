from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

class LendingOffer(db.Model,UserMixin):
    __tablename__='lendingOffer'
    id = db.Column(db.Integer, primary_key=True)
    lenderID=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    condition= db.Column(db.String(50), nullable=False)
    item= db.Column(db.String(200), nullable=False)
    category=db.Column(db.String(60), nullable=False)
    #image
    preferedLocation= db.Column(db.String(100), nullable=False)
    Status= db.Column(db.String(50), nullable=False)
    RulesOfUse= db.Column(db.String(200), nullable=False)
    
    lendRequests=db.relationship('LendingRequest',backref='lendingOffer',lazy=True,cascade="all, delete-orphan")
    lendingnotif = db.relationship('LendingNotification',backref='lendingOffer',lazy=True,cascade="all, delete-orphan")
    interestedUserList=db.relationship('Manager',backref='lendingOffer',uselist=False)

    def __init__(self,lenderID,condition,item,category,preferedLocation,Status,RulesOfUse):
        self.lenderID=lenderID
        self.item=item
        self.category=category
        self.condition=condition
        #image
        self.preferedLocation=preferedLocation
        self.Status=Status
        self.RulesOfUse=RulesOfUse
        

    def toJSON(self):
        return{
            'id': self.id,
            'lenderID':self.lenderID,
            'item': self.item,
            'category':self.category,
            'condition': self.condition,
            #image
            'preferedLocation':self.preferedLocation,
            'Status':self.Status,
            'RulesOfUse':self.RulesOfUse
        }