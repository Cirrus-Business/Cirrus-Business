#my attempt to make a calendar
#
from google.appengine.api import users
import main

user = users.get_current_user()


def checkForUser():
    if user:
        greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                    (user.nickname(), users.create_logout_url('/')))
    else:
        greeting = ('<a href="%s">Sign in or register</a>.' %
                    users.create_login_url('/'))
    return '<html><body>' + greeting + '</body></html>'


def showPersonSelector():
    return """<form action="/calDeets" method="post">
    <br/> <label for="name">Who are you?</label>
        <select name="name" id="name">
            <option value="bob">Bob</option>
            <option value="guy">Pete</option>
            <option value="tim">Tim</option>
            <option value="steve">Steve</option>
        </select>
        <input type="submit" value="Submit">
        </form>
        """

def showDeets(name):
    returnString = "boop"
    #this works
    for item in main.Shift.all():
        returnString += "booo"

    #doesnt do anything?
    row = main.Shift.gql("WHERE name = :1", u"tim")
    if row:
        for item in row:
            returnString += item.employee
            returnString += "<br/>"
    else:
        returnString = "none"
    return returnString