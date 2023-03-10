from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime

class Comment(db.Model, UserMixin):
    __tablename__='comment'
    id = db.Column(db.Integer, primary_key=True)
    commentedUserID = db.Column(db.Integer,db.ForeignKey('user.id'), nullable=False)
    comment=db.Column(db.String(120),nullable=False)
    

    def __init__(self,commentedUserID, comment):
        self.commentedUserID=commentedUserID
        self.comment=comment
        
        

    def toJSON(self):
        return{
            'id':self.id,
            'commentedUserID': self.commentedUserID,
            'comment': self.comment
        }