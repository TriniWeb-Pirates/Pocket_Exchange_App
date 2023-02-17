from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class AccountInfo(db.Model):
    accountID = db.Column(db.Integer, primary_key=True)
    userID =  db.Column(db.Integer,db.Foreignkey('user.id'), nullable=False)
    firstName = db.Column(db.String(80), nullable=False)
    lastName = db.Column(db.String(80), nullable=False)
    phoneNumber = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(120), nullable=False)
    Bio = db.Column(db.String(1000), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    reportsCount= db.Column(db.Integer, nullable=False)
    #profile_pic
    #notifications = db.Column(db.Array(String),nullable=false)


    def __init__(self, username, password,firstName,lastName,phoneNumber,email,city,Bio):
        self.username = username
        self.set_password(password)
        self.firstName=firstName
        self.lastName=lastName
        self.phoneNumber=phoneNumber
        self.email=email
        self.city=city
        self.Bio=Bio
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
            'Bio': self.Bio
        }

    