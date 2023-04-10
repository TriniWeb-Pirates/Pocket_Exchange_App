from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask import Flask, flash,Response
from flask_login import login_required, current_user, LoginManager
from werkzeug.utils import secure_filename


from App.controllers import (
    create_user,
    get_user_by_username, 
    get_all_users,
    get_user_TOJSON,
    get_all_users_json,
    login_user,
    authenticate,
    update_user,
    create_temp_user,
    get_temp_user,
    delete_temp_user,
    get_all_users_json,
    get_all_temp_users_json,
    get_all_temp_users,
    get_temp_user_by_username,
    get_user_by_email,
    get_user_by_phoneNumber,
    update_temp_user,
    getComments,
    uploadItem,
    uploadProfile,
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
    user2 = get_user_by_email(data1['email'])

    username=data1['username']
    password=data1['password']
    firstName=data1['firstName']
    lastName=data1['lastName']
    email=data1['email']
    if user:
        flash("Username is taken please enter a new username.")
        return redirect(url_for("user_views.getSignupPage1"))
    
    if user2:
        flash('This Email address is already taken. Please enter a new email address')
        return redirect(url_for("user_views.getSignupPage1"))
    #otherwise go ahead and create new temp user 
    
    temp_users = get_all_temp_users()

    if(temp_users==None):
        temp_user = create_temp_user(username, firstName, lastName, password, email)
    else:
        intermediate = temp_users.pop()
        id = intermediate.id
        temp_user = update_temp_user(id, username, firstName, lastName, password, email)
    

    return redirect(url_for('user_views.getSignupPage2',id=temp_user.id))

#Route to display the second signup page
@user_views.route('/signupPage2/<id>',methods=['GET'])
def getSignupPage2(id):
    return render_template("signup2.html",id=id)

#Route to capture the data from the second signup page and create User object
@user_views.route('/add_User_Page2/<id>',methods=['POST'])
def create_user_page2(id):
    data2=request.form

    user = get_user_by_phoneNumber(data2['phoneNumber'])
    if(user):
        flash('This phone number is already taken. Please enter a different number.')
        return redirect(url_for("user_views.getSignupPage2", id=id))

    pic=request.files["profile_pic"] #actual picture 
    if(pic):
        profile_pic=secure_filename(pic.filename) #actual filename 

  
    #storing our images here 
    if pic:
        imageURL = uploadProfile(pic, profile_pic) #once a picture has been uploaded, send to firebase and get URL
    else:
        imageURL = None


    #temp user code here now
    temp_user = get_temp_user(id)
    user=create_user(temp_user.username, temp_user.password, temp_user.firstName, temp_user.lastName, temp_user.email,data2["phoneNumber"],  data2['city'], data2['Bio'], data2['links'], imageURL)  
    delete_temp_user(id)
    
    users = get_all_users_json()
    print(users)

    temp_users = get_all_temp_users_json
    if(temp_users):
        print(temp_users)
    print('All temp users have been deleted')

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
@user_views.route('/homepage', methods=['GET'])
@login_required
def gethomepage():
    
    return render_template("homepage.html", selection=None, offers=None, search=None, user=current_user)

#route for user profile
@user_views.route('/myprofilepage', methods=['GET'])
def getprofilepage():
    userData=get_user_TOJSON(current_user.id)
    comments=getComments(current_user.id)
    print(comments)
    return render_template("ProfilePage.html",user=userData,myID=current_user.id,comments=comments)

@user_views.route('/UserProfilePage/<id>', methods=['GET'])
def getUserProfilepage(id):
    userData=get_user_TOJSON(id)
    comments=getComments(id)
    if userData != None:
        return render_template("ProfilePage.html",user=userData,myID=current_user.id, comments=comments)
    else:
        flash("User has been deleted.")
        return redirect(url_for("user_views.gethomepage"))




#Testing routes
#Route to test create user function in Postman
@user_views.route('/testAddUser',methods=['POST'])
def testAddUser():
    data1=request.json
    user=get_user_by_username(data1['username'])
    if user:
        flash("Username is taken please enter a new username.")
        return jsonify("Username is taken please enter a new username.")
    user=create_user(data1['username'], data1['password'], data1['firstName'], data1['lastName'], data1['phoneNumber'],data1['email'], data1['city'], data1['Bio'], data1['links'],data1['imageURL'])
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
    user=update_user(1,data['username'],data['password'],data['firstName'],data['lastName'],data['email'],data['phoneNumber'],data['city'],data['Bio'],data['links'],data['imageURL'])
    return jsonify(user)


#Route to retrieve all user objects in the database
@user_views.route('/getAllUsers', methods=['GET'])
def get_user_page():
    users = get_all_users_json()
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