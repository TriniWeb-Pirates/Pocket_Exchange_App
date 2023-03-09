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

myitems_views = Blueprint('myitems_views', __name__, template_folder='../templates')

@myitems_views.route('/myitems', methods=['GET'])
def getmyitems():
    return render_template("MyItems.html")
