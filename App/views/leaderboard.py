from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash,Response
from flask_login import login_required, current_user, LoginManager
from werkzeug.utils import secure_filename


#from flask_jwt import jwt_required, current_identity

#testing commit hello this is a user called User


from App.controllers import (
    createLeaderboard
)

leaderboard_views = Blueprint('leaderboard_views', __name__, template_folder='../templates')

@leaderboard_views.route('/leaderboard', methods=['GET'])
def getleaderboard():
    items=createLeaderboard()
    #return jsonify(items
    return render_template("LeaderBoard.html",items=items)



