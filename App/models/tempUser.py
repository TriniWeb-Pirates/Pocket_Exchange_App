from App.database import db

class TempUser(db.Model):
    __tablename__='tempUser'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    firstName = db.Column(db.String, nullable=False)
    lastName = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __init__(self,username, firstName, lastName, password, email):
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email

    def toJSON(self):
        return{
            'id':self.id,
            'username':self.username,
            'firstName':self.firstName,
            'lastName':self.lastName,
            'password':self.password,
            'email':self.email
        }


