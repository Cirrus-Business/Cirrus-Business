from google.appengine.ext import db

class Employee(db.Model):
    firstName = db.StringProperty(required=True)
    lastName = db.StringProperty(required=True)
    streetAddress = db.StringProperty()
    suburb = db.StringProperty()
    state = db.StringProperty()
    mobile = db.StringProperty()
    #user the user_id for logged in user and check against this to get current user deets 
    userID = db.StringProperty(required=True)
    email = db.StringProperty(required=True)
    dollarsPerHour = db.FloatProperty(required=True)

class Shift(db.Model):
    userID = db.StringProperty(required=True)
    startDate = db.DateProperty()
    startTime = db.TimeProperty()
    endDate = db.DateProperty()
    endTime = db.TimeProperty()
    paid = db.BooleanProperty()