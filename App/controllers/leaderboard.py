from App.models import User
from App.database import db

from App.controllers import (
    get_all_users_json
)

#Variable for setting the limit of profiles to be displayed
size=10
def leaderboardCriteria(users):
    return users['rating']

#Funtion to sort users and create the leaderboard
def createLeaderboard():
    count=0
    leaderboard=[]
    users=get_all_users_json()
    users.sort(reverse=True,key=leaderboardCriteria)
    for user in users:
        count=count+1
    if(count<=10):
        for i in range(count):
            leaderboard.append(users[i])
        return leaderboard
    for i in range(10):
        leaderboard.append(users[i])
    return leaderboard