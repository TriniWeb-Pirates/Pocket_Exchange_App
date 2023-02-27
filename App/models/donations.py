from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime


class Donation(db.Model):   
    itemID = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.String(120), nullable=False)

    def __init__(self,donatorID ):
        self.itemID = itemID
        self.userID = userID
        self.condition = condition
       
        
        

    def toJSON(self):
        return{

        }