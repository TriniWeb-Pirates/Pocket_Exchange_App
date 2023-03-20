from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash
from flask_login import login_required, current_user, LoginManager
from datetime import datetime

from App.controllers import (
    createReportNotification
)

reportingNotification_views = Blueprint('reportingNotification_views', __name__, template_folder='../templates')


#Test Routes
@reportingNotification_views.route('/testCreateReportNotificationPage',methods=['POST'])
@login_required
def testMakeReportNotificationPage():
    data=request.json
    notification=createNotification(data['userID'])
    return jsonify(notification)