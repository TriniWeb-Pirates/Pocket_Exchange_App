from App.models import User
from App.database import db

from App.controllers import (
    get_all_users_json
)
size=10
def leaderboardCriteria(users):
    return users['rating']

def createLeaderboard():
    users=get_all_users_json()
    users.sort(reverse=True,key=leaderboardCriteria)
    return users