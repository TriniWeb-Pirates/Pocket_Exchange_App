from abc import ABC, abstractmethod
from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db
import datetime
from abc import ABC, abstractmethod

class Request(db.Model,ABC):
    @abstractmethod
    def makeRequest(self):
        pass

