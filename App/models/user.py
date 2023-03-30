from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin



class User(db.Model,UserMixin):
    __tablename__='user'
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    phoneNumber = db.Column(db.String(20), unique=True,nullable=False)
    city = db.Column(db.String(60), nullable=False)
    Bio = db.Column(db.String(1000), nullable=False)
    links = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    reportsCount= db.Column(db.Integer, nullable=False)
    profile_pic= db.Column(db.Text, nullable=True)
    picName=db.Column(db.Text,nullable=True)
    mimetype=db.Column(db.Text, nullable=True)
    
    comments=db.relationship('Comment',backref='user',lazy=True,cascade="all, delete-orphan")
    lenderOffers=db.relationship('LendingOffer',backref='user',lazy=True,cascade="all, delete-orphan")
    lendingRequests=db.relationship('LendingRequest',backref='user',lazy=True,cascade="all, delete-orphan")
    rates=db.relationship('Rating',backref='user',lazy=True,cascade="all, delete-orphan")
    lendingnotif=db.relationship('LendingNotification',backref='user',lazy=True,cascade="all, delete-orphan")
    reports=db.relationship('Report',backref='user',lazy=True,cascade="all, delete-orphan")
    
    #accounts=db.relationship('AccountInfo',backref='accountInfo',lazy=True,cascade="all, delete-orphan")
    #communication=db.relationship('Message',backref='message',lazy=True,cascade="all, delete-orphan")
    #donators=db.relationship('DonationRequest',backref='donationRequest',lazy=True,cascade="all, delete-orphan")

    def __init__(self, username, password,firstName,lastName,phoneNumber,email,city,Bio,links,profile_pic,picName,mimetype):
        self.username = username
        self.set_password(password)
        self.firstName=firstName
        self.lastName=lastName
        self.phoneNumber=phoneNumber
        self.email=email
        self.city=city
        self.Bio=Bio
        self.links=links
        self.profile_pic=profile_pic
        self.picName=picName
        self.mimetype=mimetype
        self.rating=0
        self.reportsCount=0
        #self.profile_pic=profile_pic

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'phoneNumber': self.phoneNumber,
            'email': self.email,
            'rating': self.rating,
            'city': self.city,
            'Bio': self.Bio,
            'links':self.links,
            'reportsCount':self.reportsCount,
            'profile_pic': self.profile_pic,#testing for rendering
            'picName':self.picName
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

