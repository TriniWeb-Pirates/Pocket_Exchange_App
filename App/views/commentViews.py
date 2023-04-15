from flask import Blueprint, request, jsonify, render_template, flash, redirect, url_for
from flask_login import current_user
#from models import Comment

comment_views = Blueprint('comment_views',__name__, template_folder='../templates')

from App.controllers import (
    createComment,
    getComments,
    get_user_TOJSON
)

@comment_views.route('/add_comments/<id>', methods=['POST'])
def add_comment(id):
    message = request.form['comment']
    comment = createComment(id, message)

    flash('Comment added successfully')
    return redirect(url_for('user_views.getUserProfilepage', id=id))

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

@comment_views.route('/testAdd_comments', methods=['POST'])
def testAdd_comment():
    data = request.json
    comment = createComment(data['commentedUserID'], data['comment'])
    return jsonify(comment.toJSON(),'Comment added successfully')