from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash,Response
from flask_login import login_required, current_user, LoginManager
from werkzeug.utils import secure_filename


#from flask_jwt import jwt_required, current_identity

#testing commit hello this is a user called User


from App.controllers import (
    create_user,
    get_user_by_username, 
    get_all_users,
    get_all_users_json,
    login_user,
    authenticate
)

leaderboard_views = Blueprint('leaderboard_views', __name__, template_folder='../templates')

@leaderboard_views.route('/leaderboard', methods=['GET'])
def getleaderboard():
    return render_template("LeaderBoard.html")



#@user_views.route('/identify', methods=['GET'])
#@jwt_required()
#def identify_user_action():
#    return jsonify({'message': f"username: {current_identity.username}, id : {current_identity.id}"})

#@user_views.route('/static/users', methods=['GET'])
#def static_user_page():
#  return send_from_directory('static', 'static-user.html')
