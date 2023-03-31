import pyrebase
config = { 
     'apiKey': "AIzaSyB5JtayBsNkSaI7zU2-Sv6ymaW8nkIWo78",
     'authDomain': "info-3604-final-year-project.firebaseapp.com",
     'projectId': "info-3604-final-year-project",
     'storageBucket': "info-3604-final-year-project.appspot.com",
     'databaseURL':"info-3604-final-year-project.appspot.com" }

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

def uploadProfile(pic, profile_pic):
    storage.child(f'profile_pictures/{profile_pic}').put(pic)
    return  storage.child(f'profile_pictures/{profile_pic}').get_url(None)


def uploadItem(pic, itemPicName):
    storage.child(f'item_images/{itemPicName}').put(pic)
    return  storage.child(f'item_images/{itemPicName}').get_url(None)

