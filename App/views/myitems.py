from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash,Response
from flask_login import login_required, current_user, LoginManager
from werkzeug.utils import secure_filename

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

#Route to display myItems page
@myitems_views.route('/myitems', methods=['GET'])
def getmyitems():
    return render_template("MyItems.html")

@myitems_views.route('/myLendingOffers', methods=['GET'])
def getmylendingoffers():
    return render_template("myLendingOffers.html")

@myitems_views.route('/myBorrowRequests', methods=['GET'])
def getmyborrowrequests():
    return render_template("myBorrowRequests.html")
