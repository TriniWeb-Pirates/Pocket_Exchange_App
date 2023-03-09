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
    authenticate,
    update_user
)

user_views = Blueprint('user_views', __name__, template_folder='../templates')

#Route to display first signup page
@user_views.route('/sign', methods=['GET'])
def getSignupPage1():
    return render_template("signup.html")

#Route to capture the data from the first signup page 
@user_views.route('/add_User_Page1',methods=['POST'])
def create_user_page1():
    data1=request.form
    user=get_user_by_username(data1['username'])
    username=data1['username']
    password=data1['password']
    firstName=data1['firstName']
    lastName=data1['lastName']
    email=data1['email']
    if user:
        flash("Username is taken please enter a new username.")
        return redirect(url_for("user_views.getSignupPage1"))
    return redirect(url_for('user_views.getSignupPage2',username=username,password=password,firstName=firstName,lastName=lastName,email=email))

#Route to display the second signup page
@user_views.route('/signupPage2<username>,<password>,<firstName>,<lastName>,<email>',methods=['GET'])
def getSignupPage2(username,password,firstName,lastName,email):
    return render_template("signup2.html",username=username,password=password,firstName=firstName,lastName=lastName,email=email)

#Route to capture the data from the second signup page and create User object
@user_views.route('/add_User_Page2<username>,<password>,<firstName>,<lastName>,<email>',methods=['POST'])
def create_user_page2(username,password,firstName,lastName,email):
    data2=request.form
    pic=request.files["profile_pic"]
    profile_pic=secure_filename(pic.filename)
    mimetype=pic.mimetype    
    user=create_user(username,password,firstName,lastName,email,data2["phoneNumber"],  data2['city'], data2['Bio'], data2['links'],profile_pic=pic.read(),picName=profile_pic,mimetype=mimetype)               
    return redirect(url_for("user_views.getLoginPage"))

#Route to display the login page
@user_views.route('/loginPage', methods=["GET"])
def getLoginPage():
    return render_template("LoginPage.html")

#Route to capture the data from the login page and authenticate user
@user_views.route('/login',methods=['POST'])
def loginUser():
    data=request.form
    permittedUser=authenticate(data['username'], data['password'])
    if permittedUser==None:
        flash("Wrong Credentials, Please try again")
        return redirect(url_for('user_views.getLoginPage'))
    login_user(permittedUser,remember=True)
    flash('You were successfully logged in!')
    return redirect(url_for("user_views.gethomepage", id=permittedUser.id))

#Route to capture new profile data to update user profile 
@user_views.route('/UpdateUserProfile/<id>',methods=['PUT'])
@login_required
def UpdateUser(id):
    data=request.form
    user=update_user(id,data['username'],data['password'],data['firstName'],data['lastName'],data['email'],data['phoneNumber'],data['city'],data['Bio'],data['links'],data['profile_pic'],data['picName'],data['mimetype'])
    return redirect(url_for('user_views.gethomepage',id=id))

#Route to display the homepage to the user after login in
@user_views.route('/homepage/<id>', methods=['GET'])
@login_required
def gethomepage(id):
    return render_template("homepage.html")

#route for user profile
@profilepage_views.route('/profilepage', methods=['GET'])
def getprofilepage():
    return render_template("ProfilePage.html")


#Testing routes
#Route to test create user function in Postman
@user_views.route('/testAddUser',methods=['POST'])
def testAddUser():
    data1=request.json
    user=get_user_by_username(data1['username'])
    if user:
        flash("Username is taken please enter a new username.")
        return jsonify("Username is taken please enter a new username.")
    user=create_user(data1['username'], data1['password'], data1['firstName'], data1['lastName'], data1['phoneNumber'],data1['email'], data1['city'], data1['Bio'], data1['links'],data1['profile_pic'],data1['picName'],data1['mimetype'])
    print(user.firstName)
    return jsonify(user.id)

#Route to test login in Postman
@user_views.route('/TestLogin',methods=['POST'])
def TestloginUser():
    data=request.json
    permittedUser=authenticate(data['username'], data['password'])
    if permittedUser==None:
        flash("Wrong Credentials, Please try again")
        return jsonify("Error invalid credentials")
    login_user(permittedUser,remember=True)
    flash('You were successfully logged in!')
    return jsonify(permittedUser.username)
    #return redirect(url_for(''))

#Route to test update user function in Postman
@user_views.route('/testUpdateUserProfile',methods=['PUT'])
@login_required
def testUpdateUser():
    data=request.json
    user=update_user(1,data['username'],data['password'],data['firstName'],data['lastName'],data['email'],data['phoneNumber'],data['city'],data['Bio'],data['links'],data['profile_pic'],data['picName'],data['mimetype'])
    return jsonify(user)


#Route to retrieve all user objects in the database
@user_views.route('/getAllUsers', methods=['GET'])
def get_user_page():
    users = get_all_users()
    return jsonify(users)

@user_views.route('/api/users', methods=['GET'])
def get_users_action():
    users = get_all_users_json()
    return jsonify(users)

@user_views.route('/api/users', methods=['POST'])
def create_user_endpoint():
    data = request.json
    create_user(data['username'], data['password'])
    return jsonify({'message': f"user {data['username']} created"})

@user_views.route('/users', methods=['POST'])
def create_user_action():
    data = request.form
    flash(f"User {data['username']} created!")
    create_user(data['username'], data['password'])
    return redirect(url_for('user_views.get_user_page'))