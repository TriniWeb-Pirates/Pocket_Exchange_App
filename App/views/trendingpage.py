from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash,Response
from flask_login import login_required, current_user, LoginManager
from werkzeug.utils import secure_filename


#from.trendingpage import trend_views

from App.controllers import (
    create_user,
    get_user_by_username, 
    get_all_users,
    get_all_users_json,
    login_user,
    authenticate
)

trend_views = Blueprint('trend_views', __name__, template_folder='../templates')

#Route to display trending page
@trend_views.route('/trending_page', methods=['GET'])
def gettrendpage():
    return render_template("TrendingPage.html")


