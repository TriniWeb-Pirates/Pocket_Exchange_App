from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class Manager(db.Model):
    __tablename__='manager'
    id = db.Column(db.Integer, primary_key=True)
    

   # def __init__(self,):
        

    def toJSON(self):
        return{
            'Managerid': self.Managerid,
        }