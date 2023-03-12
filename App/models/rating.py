from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


class Rating(db.Model,UserMixin):
    __tablename__='rating'
    id = db.Column(db.Integer, primary_key=True)
    recipientID=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    rate=db.Column(db.Integer,nullable=False)
    

    def __init__(self,recipientID, rate):
        self.recipientID=recipientID
        self.rate=rate
        
        

    def toJSON(self):
        return{
            'id': self.id,
            'recipientID': self.recipientID,
            'rate': self.rate
        }