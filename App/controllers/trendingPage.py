from App.models import LendingOffer,LendingRequest,User
from App.database import db

TrendingDict={
    "username":"",
    "Item_Name":"",
    "requestCount":0
}

def trendingItemsCriteria(data):
    return data['requestCount']

def buildTredingList():
    itemList=[]
    trendingList=[]
    offers=LendingOffer.query.all()
    items = [offer.toJSON() for offer in offers]
    for item in items:
        user=User.query.get(item['lenderID'])
        username=user.username
        count=0
        requests=LendingRequest.query.filter_by(lendingoffer_ID=item['id']).all()
        info = [request.toJSON() for request in requests]
        for data in info:
            count=count+1
        obj=dict(username=username,Item_Name=item['item'],requestCount=count)
        trendingList.append(obj)

    trendingList.sort(reverse=True,key=trendingItemsCriteria)
    for i in range(10):
        itemList.append(trendingList[i])
    return itemList
