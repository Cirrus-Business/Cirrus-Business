from google.appengine.ext import db
from google.appengine.api import users

class Employee(db.Model):
    firstName = db.StringProperty(required=true)
    lastName = db.StringProperty(required=true)
    streetAddress = db.StringProperty()
    suburb = db.StringProperty()
    state = db.StringProperty()
    mobile = db.StringProperty()
    #user the user_id for logged in user and check against this to get current user deets 
    userID = db.StringProperty(required=true)
    email = db.StringProperty(required=true)
    dollarsPerHour = db.FloatProperty(required=true)

class Shift(db.Model):
    userID = db.StringProperty(required=true)
    startDate = db.DateProperty()
    startTime = db.TimeProperty()
    endDate = db.DateProperty()
    endTime = db.TimeProperty()
    paid = db.BooleanProperty()