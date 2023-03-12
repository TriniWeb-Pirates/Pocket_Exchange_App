from App.models import Comment,User
from App.database import db

def createComment(commentedUserID,comment):
    newComment = Comment(commentedUserID=commentedUserID,comment=comment)
    db.session.add(newComment)
    db.session.commit()
    return newComment

def getComments(comment):
    comments = Comment.query.filter_by(comment=comment).all()
    return comments