from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class LendingOffer(db.Model):
    OfferID = db.Column(db.Integer, primary_key=True)
    lenderID=db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    condition= db.Column(db.String(50), nullable=False)
    item= db.Column(db.String(60), nullable=False)
    #image
    preferedLocation= db.Column(db.String(100), nullable=False)
    Status= db.Column(db.String(50), nullable=False)
    RulesOfUse= db.Column(db.String(200), nullable=False)
    

    def __init__(self,lenderID,condition,item,preferedLocation,Status,RulesOfUse):
        self.lenderID=lenderID
        self.condition=condition
        self.item=item
        #image
        self.preferedLocation=preferedLocation
        self.Status=Status
        self.RulesOfUse=RulesOfUse
        

    def toJSON(self):
        return{
            'Managerid': self.Managerid,
            'lenderID':self.lenderID,
            'condition': self.condition,
            'item': self.item,
            #image
            'preferedLocation':self.preferedLocation,
            'Status':self.Status,
            'RulesOfUse':self.RulesOfUse
        }