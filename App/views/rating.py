from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager

from App.controllers import (
    createRating,
    retieveAllRatings
)

rating_views = Blueprint('rating_views', __name__, template_folder='../templates')


#Testing Routes
#Route to capture rating data and rate an experience with another user
@rating_views.route('/testAddRating',methods=['POST'])
@login_required
def testAddRatingFunc():
    data=request.json
    print(data['recipientID'])
    response=createRating(data['recipientID'],data['rate'])
    #print(response.rate)
    return jsonify(response.rate)

@rating_views.route('/testDisplayAllRatings',methods=['GET'])
@login_required
def testGetAllRatingsFunc():
    ratings=retieveAllRatings()
    #print(response.rate)
    return jsonify(ratings)