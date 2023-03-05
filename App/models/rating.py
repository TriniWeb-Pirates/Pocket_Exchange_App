from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime

class Rating(db.Model):
    __tablename__='rating'
    rateID = db.Column(db.Integer, primary_key=True)
    ratedUserID =  db.Column(db.Integer, db.Foreignkey('user.id'), nullable=False)
    rate=db.Column(db.Integer,nullable=False)
    

    def __init__(self,ratedUserID, rate):
        self.ratedUserID=ratedUserID
        self.rate=rate
        
        

    def toJSON(self):
        return{
            'rateID': self.rateID,
            'ratedUserID': self.ratedUserID,
            'rate': self.rate
        }