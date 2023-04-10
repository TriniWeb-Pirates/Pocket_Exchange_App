from App.models import Comment,User
from App.database import db

#testing new acccount

def createComment(commentedUserID,comment):
    newComment = Comment(commentedUserID=commentedUserID,comment=comment)
    db.session.add(newComment)
    print(newComment)
    db.session.commit()
    return newComment

def getComments(commentedUserID):
    comments = Comment.query.filter_by(commentedUserID=commentedUserID).all()
    if comments:
        results = [comment.toJSON() for comment in comments]
    else:
        results=None
    #print(results)
    return results