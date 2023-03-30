from App.models import Comment,User
from App.database import db

def createComment(commentedUserID,comment):
    newComment = Comment(commentedUserID=commentedUserID,comment=comment)
    db.session.add(newComment)
    db.session.commit()
    return newComment

def getComments(commentedUserID):
    comments = Comment.query.filter_by(commentedUserID=commentedUserID).all()
    results = [comment.toJSON() for comment in comments]
    print(results)
    return results