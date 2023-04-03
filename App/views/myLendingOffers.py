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

myLendingOffers_views = Blueprint('myLendingOffers_views', __name__, template_folder='../templates')

#Route to display myItems page

@myLendingOffers_views.route('/myLendingOffers', methods=['GET'])
def getmylendingoffers():
    return render_template("myLendingOffers.html")
