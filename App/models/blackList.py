from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

class BlockedUser(db.Model):
    __tablename__='blockedUser'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=False,nullable=False)
    phoneNumber = db.Column(db.String(20), unique=False,nullable=False)

    def __init__(self, phoneNumber,email):
        self.phoneNumber=phoneNumber
        self.email=email

    def toJSON(self):
        return{
            'id': self.id,
            'phoneNumber': self.phoneNumber,
            'email': self.email
        }