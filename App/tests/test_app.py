import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date, datetime, timedelta
from App.main import create_app
from App.database import create_db
from App.models import User,LendingOffer,LendingNotification,Manager,LendingRequest,Rating,Report,Comment,BlockedUser,TempUser,ReportNotification
from App.controllers import (
    create_user,
    create_lendingOffer,
    create_lendingRequest,
    create_lendingRequest_for_testing,
    createRating,
    create_report,
    buildTredingList,
    deleteLendingRequest,
    getItmesByCategory,
    addToList,
    createNotification,
    createLeaderboard,
    createComment,
    makeReportNotification,
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
    UnapproveTemp,
    changeStatus,
    deleteLendingRequest,
    countRequests,
    createLeaderboard,
    restartOffer,
    remove_Offer,
    get_offer_by_ID
)

from wsgi import app


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UserUnitTests(unittest.TestCase):
    maxDiff=None

    def test_new_user(self):
        user = User("bob", "bobpass","bobby","brown","bob@gmail.com",443-7890,"Arima","I like cars","www.bobbyPage.com",None)
        assert user.username == "bob"

    #pure function no side effects or integrations called
    def testUser_toJSON(self):
        user = User("bob", "bobpass","bobby","brown",443-7890,"bob@gmail.com","Arima","I like cars","www.bobbyPage.com",None)
        user_json = user.toJSON()
        self.assertDictEqual(user_json, {"id":None, "username":"bob","firstName":"bobby","lastName":"brown","email":"bob@gmail.com","phoneNumber":443-7890,"city":"Arima","Bio":"I like cars","links":"www.bobbyPage.com","rating":0,"reportsCount":0,"imageURL":None})
    
    def test_lendingOffer_toJSON(self):
        user = create_user("leroy", "bobpass","bobby","brown","leroy@gmail.com",892233851,"Arima","I like cars","www.bobbyPage.com",None)
        offer=create_lendingOffer(1,"pencilTypeB","Stationary","writes with ink",None,"Do not break it","good","Arima",)
        data=offer.toJSON()
        assert data['item']=="penciltypeb" and data['category']=="Stationary"
    
    
    def test_lendingRequest_toJSON(self):
        user = create_user("lion", "bobpass","bobby","brown","lion@gmail.com",892233877,"Arima","I like cars","www.bobbyPage.com",None)
        lendingRequest=create_lendingRequest_for_testing(2,1,"i need it for exams","arima")
        remove_Offer(1)
        data=lendingRequest
        assert data['preferedLocation']=="arima" and data['reasonForUse']=="i need it for exams"

    def test_report_toJSON(self):
        report=Report(2,"He broke my lawnmower")
        data=report.toJSON()
        assert data['description']=="He broke my lawnmower"

    def test_rating_toJSON(self):
        rating=Rating(1,5)
        data=rating.toJSON()
        assert data['rate']==5
    
    def test_BlockedUser_toJSON(self):
        user=BlockedUser(443-7890,"bob@gmail.com")
        data=user.toJSON()
        assert data['email']=="bob@gmail.com"
    
    def test_Comment_toJSON(self):
        comment=Comment(2,"This person is very kind")
        data=comment.toJSON()
        assert data['comment']=="This person is very kind"

    def test_TempUser_toJSON(self):
        temp=TempUser("kelly","mint","fire","pass","f@gmail.com")
        data=temp.toJSON()
        assert data['username']=="kelly" and data['password']=="pass"

    def test_ReportNotification_toJSON(self):
        reportNotif=ReportNotification(1,"This user has been reported")
        data=reportNotif.toJSON()
        assert data['notification']=="This user has been reported"
    
    def test_LendingNotification_toJSON(self):
        lendNotif=LendingNotification(1,2,"pen is no longer available")
        data=lendNotif.toJSON()
        assert data['notification']=="pen is no longer available"

    def test_Manager_toJSON(self):
        info=Manager(1,"2,3,4")
        data=info.toJSON()
        assert data['InterestedUserList']=="2,3,4"

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
        
        assert lendingRequest=="Borrow request created successfully. You can see the status of your request in the My Items Page > My Borrow Requests. "
    
    def test_addToList(self):
        userList=addToList(2,1)
        assert userList.lendingOfferID==1

    def test_grantTempApproval(self):
        requestData=grantTempApproval(1,1,1)
        assert requestData!=None

    def test_setDates(self):
        offer=create_lendingOffer(1,"pen","Stationary","writes with ink",None,"Do not break it","good","Arima",)
        lendingRequest=create_lendingRequest(1,2,"i need it for exams","arima")
        #print(lendingRequest)
        #requestData=grantTempApproval(1,1,1)
        offer=setDates(1,1,"2022-07-12","2022-07-09")
        #assert offer.returnDate==date(2022,7,12)
        assert offer=="Action Denied, this lending request must be temporarily approved first"

    def test_findItems(self):
        findings=findItems("Pen")
        assert findings!=None
    
    def test_createRating(self):
        user = create_user("charlie", "bobpass","bobby","brown","charlie@gmail.com",882000251,"Arima","I like cars","www.bobbyPage.com",None)
        rating=createRating(2,1,5)
        assert rating['rate']==5

    def test_createNotification(self):
        userNotification=createNotification(1,1,"Pen is unavailable at this time, Please try again when it is made available")
        assert userNotification.notification=="Pen is unavailable at this time, Please try again when it is made available"

    def test_getItmesByCategory(self):
        user = create_user("timmy", "bobpass","bobby","brown","timmy@gmail.com",882954251,"Arima","I like cars","www.bobbyPage.com",None)
        offer=create_lendingOffer(2,"pen","Stationary","writes with ink",None,"Do not break it","good","Arima",)
        items=getItmesByCategory("Stationary")
        assert items[1]['item']=="pen"

    def test_create_report(self):
        report=create_report(1,2,"He broke my lawnmower")
        assert report['description']=="He broke my lawnmower"
    
    def test_makeReportNotification(self):
        message=makeReportNotification(1)
        assert message!=None
    
    def test_createComment(self):
        comment=createComment(1,"The item was very useful")
        assert comment.comment=="The item was very useful"
    
    def test_addBlackListedUser(self):
        blocked=addBlackListedUser("badGuy@gmail.com",882700259)
        assert blocked.email=="badGuy@gmail.com"
    
    def test_restartOffer(self):
        item=create_lendingOffer(2,"pencil","Stationary","writes with ink",None,"Do not break it","good","Arima",)
        offer=restartOffer(2,2)
        assert offer!="Action denied, You cannit restart this offer"
    
    def test_remove_Offer(self):
        response=remove_Offer(1)
        assert response.item=="pen"
