import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date, datetime, timedelta
from App.main import create_app
from App.database import create_db
from App.models import User
from App.controllers import (
    create_user,
    create_lendingOffer,
    create_lendingRequest,
    createRating,
    create_report,
    buildTredingList,
    addToList,
    createNotification,
    createLeaderboard,
    createComment,
    addBlackListedUser,
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
    setDates,
    findItems,
    grantTempApproval,
    UnapproveTemp

)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):

    def test_new_user(self):
        user = User("bob", "bobpass","bobby","brown","bob@gmail.com",443-7890,"Arima","I like cars","www.bobbyPage.com",None)
        assert user.username == "bob"

    # pure function no side effects or integrations called
    #def test_toJSON(self):
    #    user = User("bob", "bobpass","bobby","brown","bob@gmail.com",443-7890,"Arima","I like cars","www.bobbyPage.com",None,None,None)
    #    user_json = user.toJSON()
    #    self.assertDictEqual(user_json, {"id":None, "username":"bob","password":"bobpass","firstName":"bobby","lastName":"brown","email":"bob@gmail.com","phoneNumber":443-7890,"city":"Arima","Bio":"I like cars","links":"www.bobbyPage.com","rating":0,"reportsCount":0,"profile_pic":None,"picName":None,"mimetype":None})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        user = User("bob", password,"bobby","brown","bob@gmail.com",443-7890,"Arima","I like cars","www.bobbyPage.com",None)
        assert user.password != password

    def test_check_password(self):
        password = "mypass"
        user = User("bob", password,"bobby","brown","bob@gmail.com",443-7890,"Arima","I like cars","www.bobbyPage.com",None)
        assert user.check_password(password)
    


'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app.config.update({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db(app)
    yield app.test_client()
    os.unlink(os.getcwd()+'/App/test.db')


#def test_authenticate():
#    user = create_user("bob", "bobpass")
#    assert authenticate("bob", "bobpass") != None

class UsersIntegrationTests(unittest.TestCase):

    def test_create_user(self):
        user = create_user("rick", "bobpass","bobby","brown","bike@gmail.com",892200851,"Arima","I like cars","www.bobbyPage.com",None)
        assert user.username == "rick"

    def test_create_lendingOffer(self):
        offer=create_lendingOffer(1,"pen","Stationary","writes with ink",None,"Do not break it","good","Arima",)
        assert offer.item=="pen"

    

    def test_create_lendingRequest(self):
        user = create_user("mike", "bobpass","bobby","brown","mike@gmail.com",192000251,"Arima","I like cars","www.bobbyPage.com",None)
        lendingRequest=create_lendingRequest(2,1,"i need it for exams","arima")
        assert lendingRequest=="Borrow request created"
    
    def test_grantTempApproval(self):
        requestData=grantTempApproval(1,1,1)
        assert requestData=="Approval Granted"
    
    def test_UnapproveTemp(self):
        user = create_user("marcus", "bobpass","bobby","brown","marcus@gmail.com",182470251,"Arima","I like cars","www.bobbyPage.com",None)
        lendingRequest=create_lendingRequest(3,1,"i need it for exams","arima")
        request=UnapproveTemp(2,1)
        assert request.tempApproval==False

    def test_setDates(self):
        offer=setDates(1,1,"2022-07-12","2022-07-09")
        assert offer.returnDate==date(2022,7,12)
    
    def test_findItems(self):
        findings=findItems("Pen")
        assert findings!=None
    
    def test_createRating(self):
        user = create_user("charlie", "bobpass","bobby","brown","charlie@gmail.com",882000251,"Arima","I like cars","www.bobbyPage.com",None)
        rating=createRating(2,1,5)
        print(rating)
        assert rating.rate==5
    
    def test_create_report(self):
        report=create_report(1,2,"He broke my lawnmower")
        assert report['description']=="He broke my lawnmower"

    #def test_get_all_users_json(self):
    #    users_json = get_all_users_json()
    #    self.assertListEqual([{"id":1, "username":"bob"}, {"id":2, "username":"rick"}], users_json)

    # Tests data changes in the database
    #def test_update_user(self):
    #    update_user(1, "ronnie","bobpass","bobby","brown","bob@gmail.com",443-7890,"Arima","I like cars","www.bobbyPage.com",None,None,None)
    #    user = get_user_by_username("ronnie")
    #    assert user.username == "ronnie"
