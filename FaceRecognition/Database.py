import pyrebase
import datetime
config = {
    "apiKey": "AIzaSyAcGiqfnh4GJ8maZXZrOsibdKQK_Yxrsbo",
    "authDomain": "facregattendence.firebaseapp.com",
    "projectId": "facregattendence",
    "databaseURL":"https://facregattendence-default-rtdb.firebaseio.com",
    "storageBucket": "facregattendence.appspot.com",
    "ServiceAccount":"ServiceAccountKey.json"
}
def Addperson(rollno):
    today = datetime.date.today().strftime('%d-%m-%Y')
    print(today)
    firebase=pyrebase.initialize_app(config)
    db=firebase.database()
    db.child('students').child(today).update({rollno:"Added"})
def markpresent(rollno):
    today = datetime.date.today().strftime('%d-%m-%Y')
    firebase=pyrebase.initialize_app(config)
    db=firebase.database()
    #print(today)
    db.child("students").child(today).update({rollno:'present'})
def markabsent(rollno):
    today = datetime.date.today().strftime('%d-%m-%Y')
    firebase=pyrebase.initialize_app(config)
    db=firebase.database()
    #print(today)
    db.child("students").child(today).update({rollno:'absent'})
