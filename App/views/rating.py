from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager

from App.controllers import (
    createRating,
    retieveAllRatings,
    updateRating
)

rating_views = Blueprint('rating_views', __name__, template_folder='../templates')

@rating_views.route('/AddRating/<recipientID>',methods=['POST'])
@login_required
def AddRatingFunc(recipientID):
    data=request.form
    response=createRating(recipientID,data['rate'])
    #return redirect(url_for())
    return jsonify(response.rate)



#Testing Routes
#Route to capture rating data and rate an experience with another user
@rating_views.route('/testAddRating/<id>/<recipientID>',methods=['POST'])
@login_required
def testAddRatingFunc(id,recipientID):
    data=request.json
    response=createRating(data['id'],data['recipientID'],data['rate'])
    return jsonify(response)

@rating_views.route('/testDisplayAllRatings',methods=['GET'])
@login_required
def testGetAllRatingsFunc():
    ratings=retieveAllRatings()
    #print(response.rate)
    return jsonify(ratings)

@rating_views.route('/testUpdateRating/<id>',methods=['PUT'])
@login_required
def testUpdateRatingFunc(id):
    data=request.json
    #print(id)
    response=updateRating(data['id'],data['rate'])
    #return redirect(url_for())
    return jsonify(response.rate)