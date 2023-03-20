from App.models import User
from App.database import db

from App.controllers import (
    get_all_users_json
)
size=10

def createLeaderboard():
    users=get_all_users_json()
    info=users.sort(reverse=True,key=leaderboardCriteria())
    print(info)
    return info

def leaderboardCriteria(data):
    return data['rating']


