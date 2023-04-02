from App.models import LendingOffer,LendingRequest,User
from App.database import db

TrendingDict={
    "username":"",
    "Item_Name":"",
    "requestCount":0,
    'imageURL':"imageURL"
}

def trendingItemsCriteria(data):
    return data['requestCount']

def buildTredingList():
    itemList=[]
    trendingList=[]
    offers=LendingOffer.query.all()
    items = [offer.toJSON2() for offer in offers]
    for item in items:
        user=User.query.get(item['lenderID'])
        username=user.username
        count=0
        imageURL=item['imageURL']
        
        requests=LendingRequest.query.filter_by(lendingoffer_ID=item['id']).all()
        info = [request.toJSON() for request in requests]
        for data in info:
            count=count+1
        obj=dict(username=username,Item_Name=item['item'],requestCount=count,imageURL=imageURL)
        trendingList.append(obj)

    trendingList.sort(reverse=True,key=trendingItemsCriteria)
    num=0
    for item in trendingList:
        num=num+1
    if(num<10):
        for i in range(num):
            itemList.append(trendingList[i])
    else:
        for i in range(10):
            itemList.append(trendingList[i])
    return itemList
