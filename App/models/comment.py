from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime

class Comment(db.Model):
    commentID = db.Column(db.Integer, primary_key=True)
    commentedUserID =  db.Column(db.Integer,db.Foreignkey('user.id'), nullable=False)
    comment=db.Column(db.String(120),nullable=False)
    

    def __init__(self,commentedUserID, comment):
        self.commentedUserID=commentedUserID
        self.comment=comment
        
        

    def toJSON(self):
        return{
            'commentID':self.commentID,
            'commentedUserID': self.commentedUserID,
            'comment': self.comment
        }