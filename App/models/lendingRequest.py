from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime, timedelta
from flask_login import UserMixin


class LendingRequest(db.Model,UserMixin):
    __tablename__='lendingRequest'
    id = db.Column(db.Integer, primary_key=True)
    borrowerID =  db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    lendingoffer_ID= db.Column(db.Integer,db.ForeignKey('lendingOffer.id'), nullable=False)
    reasonForUse=db.Column(db.String(300), nullable=False)
    preferedLocation= db.Column(db.String(100), nullable=False)
    Status= db.Column(db.Boolean,nullable=False)
    tempApproval=db.Column(db.Boolean,nullable=False)

    def __init__(self,borrowerID, lendingoffer_ID,reasonForUse,preferedLocation,Status,tempApproval):
        self.borrowerID=borrowerID
        self.lendingoffer_ID=lendingoffer_ID
        self.reasonForUse=reasonForUse
        self.preferedLocation=preferedLocation
        self.Status=Status
        self.tempApproval=tempApproval        

    def toJSON(self):
        return{
            "id":self.id,
            'borrowerID': self.borrowerID,
            'user': self.user.toJSON(),
            'lendingOffer':self.lendingOffer.toJSON(),
            'lendingoffer_ID': self.lendingoffer_ID,
            'reasonForUse':self.reasonForUse,
            'preferedLocation': self.preferedLocation,
            'Status': self.Status,
            'tempApproval': self.tempApproval
        }