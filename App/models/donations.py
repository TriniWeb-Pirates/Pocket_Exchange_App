from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime


class Donation(db.Model):   
    

    def __init__(self,donatorID ):
        self.donatorID=donatorID
       
        
        

    def toJSON(self):
        return{

        }