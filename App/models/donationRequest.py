from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime


class DonationRequest(db.Model):
    __tablename__='donationRequest'
    donateRequestID = db.Column(db.Integer, primary_key=True)
    donatorID =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    

    def __init__(self,donatorID ):
        self.donatorID=donatorID
       
        
        

    def toJSON(self):
        return{
            'donateRequestID': self.donateRequestID,
            'donatorID': self.donatorID,
        }