from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash,Response
from flask_login import login_required, current_user, LoginManager
from werkzeug.utils import secure_filename


from App.controllers import (
    create_user,
    get_user_by_username, 
    get_all_users,
    get_all_users_json,
    login_user,
    authenticate
)

profilepage_views = Blueprint('profilepage_views', __name__, template_folder='../templates')

#Route to display user profile page
@profilepage_views.route('/profilepage', methods=['GET'])
def getprofilepage():
    return render_template("ProfilePage.html")

