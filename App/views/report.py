from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    create_report,
    getAllBlockedUsersJSON
)

report_views = Blueprint('report_views', __name__, template_folder='../templates')


#Test Routes
@report_views.route('/testAddReport',methods=['POST'])
@login_required
def testReporting():
    data=request.json
    report=create_report(data['offenderID'],data['description'])
    return jsonify(report)

@report_views.route('/testGetAllBlocked',methods=['Get'])
@login_required
def testGetBlocked():
    blockedUsers=getAllBlockedUsersJSON()
    return jsonify(blockedUsers)