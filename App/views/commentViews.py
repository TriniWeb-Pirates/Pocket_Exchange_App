from flask import Blueprint, request, jsonify
#from models import Comment

comment_views = Blueprint('comment_views',__name__, template_folder='../templates')

from App.controllers import (
    createComment,
    getComments
)

@comment_views.route('/add_comments', methods=['POST'])
def add_comment():
    commentedUserID = request.json['commentedUserID']
    message = request.json['comment']
    comment = createComment(commentedUserID, message)
    print(comment.commentedUserID)
    return jsonify({'message': 'Comment added successfully'})

@comment_views.route('/get_comments', methods=['GET'])
def get_comments():
    comments = Comment.get_all()
    result = []
    for comment in comments:
        comment_data = {}
        comment_data['id'] = comment.id
        comment_data['name'] = comment.name
        comment_data['message'] = comment.message
        result.append(comment_data)
    return jsonify(result)