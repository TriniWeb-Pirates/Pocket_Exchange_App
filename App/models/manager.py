from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
#from flask_sqlalchemy import SQLAlchemy, ARRAY

class Manager(db.Model):
    __tablename__='manager'
    id = db.Column(db.Integer, primary_key=True)
    lendingOfferID= db.Column(db.Integer,db.ForeignKey('lendingOffer.id'), unique=True, nullable=False)
    InterestedUserList= db.Column(db.Text, nullable=True)
    #InterestedUserList=db.Column(ARRAY(Integer), nullable=True)
    def __init__(self,InterestedUserList):
        self.InterestedUserList=InterestedUserList

    def toJSON(self):
        return{
            'id': self.id,
            'InterestedUserList': self.InterestedUserList
        }