from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    create_lendingRequest, 
    get_request_by_ID,
    updateLendingRequest,
    getAllRequestsJSON,
    countRequests,
    getAllOfferRequests,
    grantTempApproval
)

lendingRequests_views = Blueprint('lendingRequests_views', __name__, template_folder='../templates')

#Route to retrieve lending request form page and limit number of requests made to 3 requests
@lendingRequests_views.route('/lendingRequestForm/<id>', methods=['GET'])
@login_required
def GetLendingRequestData(id):
    borrowerID=id
    result=countRequests(borrowerID)
    if result!=None:
        return redirect(url_for('user_views.gethomepage',id=id))
    return jsonify(result)
    #return render_template()

#Route to capture lending request data to create lending request object
@lendingRequests_views.route('/CreatelendingRequest',methods=['POST'])
@login_required
def makeLendingRequestPage():
    data=request.form
    lendRequest=create_lendingRequest(data['borrowerID'],data['lendingoffer_ID'],data['preferedLocation'],data['Status'],data['quantity'],data['tempApproval'],data['borrowingDays'],data['returnDate'],data['borrowDate'])
    return jsonify(lendRequest.borrowDate)




#testing routes
#Route to test lending request limit in Postman
@lendingRequests_views.route('/testLendingRequestForm', methods=['GET'])
@login_required
def testGetLendingRequestData():
    data=request.json
    borrowerID=data['id']
    result=countRequests(borrowerID)
    if result!=None:
        return jsonify(result)
        #return redirect(url_for('user_views.gethomepage',id=id))
    return jsonify(result)
    #return render_template()

#Route to test creating a lending request 
@lendingRequests_views.route('/testCreatelendingRequest',methods=['POST'])
@login_required
def testMakeLendingRequestPage():
    data=request.json#must change json to form for web page
    lendRequest=create_lendingRequest(data['borrowerID'],data['lendingoffer_ID'],data['preferedLocation'],data['Status'],data['quantity'],data['tempApproval'],data['borrowingDays'],data['returnDate'],data['borrowDate'])
    print(lendRequest.borrowDate)
    return redirect(url_for("manager_views.testAddUsersToList"),borrowerID=data['borrowerID'],lendingoffer_ID=data['lendingoffer_ID'])

#Route to test updating lending request object
@lendingRequests_views.route('/testUpdateLendingRequest',methods=['PUT'])
@login_required
def testUpdateLendingRequestPage():
    data=request.json
    lendRequest=updateLendingRequest(data['id'],data['borrowerID'],data['lendingoffer_ID'],data['preferedLocation'],data['Status'],data['quantity'],data['tempApproval'],data['borrowingDays'],data['borrowDate'],data['returnDate'])
    return jsonify(lendRequest.borrowDate)

#Route to test retrieving all lending request objects in the database
@lendingRequests_views.route('/testGetAllRequests', methods=['GET'])
@login_required
def testRetreiveAllRequests():
    requests=getAllRequestsJSON()
    return requests

#Route for retrieving all requests for an offer
@lendingRequests_views.route('/testGetAllOfferRequests/<lendingoffer_ID>', methods=['GET'])
@login_required
def testRetreiveOfferRequests(lendingoffer_ID):
    requests=getAllOfferRequests(lendingoffer_ID)
    return jsonify(requests) 

#Route for granting temporary approval
@lendingRequests_views.route('/testGrantTempApproval/<id>', methods=['GET'])
@login_required
def testGrantTempApproval(id):
    request=grantTempApproval(id)
    return jsonify(request.tempApproval)