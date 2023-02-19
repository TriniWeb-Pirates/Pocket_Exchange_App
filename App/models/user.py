from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    phoneNumber = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    Bio = db.Column(db.String(1000), nullable=False)
    links = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    reportsCount= db.Column(db.Integer, nullable=False)
    #profile_pic
    #notifications = db.Column(db.Array(String),nullable=false)
    accounts=db.relationship('AccountInfo',backref='accountInfo',lazy=True,cascade="all, delete-orphan")
    communication=db.relationship('Message',backref='message',lazy=True,cascade="all, delete-orphan")
    lenderOffers=db.relationship('LendingOffer',backref='lendingOffer',lazy=True,cascade="all, delete-orphan")
    donators=db.relationship('DonationRequest',backref='donationRequest',lazy=True,cascade="all, delete-orphan")
    lendingRequests=db.relationship('LendingRequest',backref='lendingRequest',lazy=True,cascade="all, delete-orphan")
    reports=db.relationship('Report',backref='report',lazy=True,cascade="all, delete-orphan")
    rates=db.relationship('Rating',backref='rating',lazy=True,cascade="all, delete-orphan")

    def __init__(self, username, password,firstName,lastName,phoneNumber,email,city,Bio,links):
        self.username = username
        self.set_password(password)
        self.firstName=firstName
        self.lastName=lastName
        self.phoneNumber=phoneNumber
        self.email=email
        self.city=city
        self.Bio=Bio
        self.links=links
        self.rating=0
        self.reportsCount=0

    def toJSON(self):
        return{
            'id': self.id,
            'username': self.username,
            'firstName': self.firstName,
            'lastName': self.lastName,
            'phoneNumber': self.phoneNumber,
            'email': self.email,
            'city': self.city,
            'Bio': self.Bio,
            'links':self.links
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

