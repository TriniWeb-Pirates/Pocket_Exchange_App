from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db



class Manager(db.Model):
    __tablename__='manager'
    id = db.Column(db.Integer, primary_key=True)
    lendingOfferID= db.Column(db.Integer,db.ForeignKey('lendingOffer.id'), unique=True, nullable=True)
    InterestedUserList= db.Column(db.Text, nullable=True)
   
    def __init__(self,lendingOfferID,InterestedUserList):
        self.lendingOfferID=lendingOfferID
        self.InterestedUserList=InterestedUserList

    def toJSON(self):
        return{
            'id': self.id,
            'lendingOfferID':self.lendingOfferID,
            'InterestedUserList': self.InterestedUserList
        }