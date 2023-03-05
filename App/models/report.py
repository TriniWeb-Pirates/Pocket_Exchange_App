from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime

class Report(db.Model):
    __tablename__='report'
    reportID = db.Column(db.Integer, primary_key=True)
    offenderID =  db.Column(db.Integer,db.Foreignkey('user.id'), nullable=False)
    description=db.Column(db.String(120),nullable=False)
    

    def __init__(self,offenderID , description):
        self.offenderID=offenderID
        self.description=description
        
        

    def toJSON(self):
        return{
            'reportID': self.reportID,
            'offenderID': self.offenderID,
            'description': self.description
        }