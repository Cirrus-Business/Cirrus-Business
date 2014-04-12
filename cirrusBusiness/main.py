#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.api.datastore import Get


FORM_PAGE =  """ 
<!doctype html>
<html>
  <body>
    <h1>Welcome to Deanbook</h1>
    <p>Please enter your shift details below</p>
    <form action="/shift" method="post">
        <label for="employees">Who are you?</label>
        <select name="employees" id="employees">
            <option value="bob">Bob</option>
            <option value="guy">Pete</option>
            <option value="tim">Tim</option>
            <option value="steve">Steve</option>
        </select>
        <br/>
        <label for="start">Enter Start date and time </label>
        <input type="text" name="start" id="start">
        <br/>
        <label for="end">Enter End date and time </label>
        <input type="text" name="end" id="end">
        <br/>
        <label for="employees">Use Current Time</label>
        <input type='button'></input>
        <br/>
        <br/>
        <input type="submit" value="Submit">
    </form>
  </body>
</html>

"""
OTHER_PAGE1 = """
    <!doctype html>
    <html>
      <body>
        <h1>Welcome to Deanbook</h1>
        <h2>Here is what you entered</h2>"""
OTHER_PAGE2 = """
        <form method="get" action="/info">
            <button type="submit">Continue</button>
        </form>
      </body>
    </html>"""

OTHER_PAGE3 = """
    <!doctype html>
    <html>
      <body>
        <h1>Welcome to Deanbook</h1>
        <h2>This is what is now in the db</h2>"""
        
OTHER_PAGE4 = """
    </body>
    </html>"""

class Shift(db.Model):
    employee = db.StringProperty()
    start = db.StringProperty()
    end = db.StringProperty()

class MainHandler(webapp2.RequestHandler):
    def get(self):
         self.response.write(FORM_PAGE)

class InfoHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(OTHER_PAGE3) 
        for p in Shift.all():
            b = p.key()
            self.response.write(b)
            self.response.write("<br/>" +p.employee)
            self.response.write("<br/>" + p.start)
            self.response.write("<br/>" + p.end + "<br/><br/>")
        
        r = Shift.gql("WHERE employee = :1", u"tim")
        self.response.write("<h2> all of the tim's</h2>") 
        i = 1 
        for j in r:
            b = j.key()
            self.response.write(b)
            self.response.write("<br/>" +j.employee)
            self.response.write("<br/>" + j.start)
            self.response.write("<br/>" + j.end + "<br/><br/>")
        self.response.write(OTHER_PAGE4)
           

class ShiftHandler(webapp2.RequestHandler):
    def post(self):
        self.response.write(OTHER_PAGE1)
        employee1 = self.request.get('employees')
        start1 = self.request.get('start')
        end1 = self.request.get('end')
        self.response.write("<p><strong>Your name is:</strong> " + employee1 + "</p>")
        self.response.write("<p><strong>The start of your shift was:</strong> " + start1 + "</p>")
        self.response.write("<p><strong>The end of your shift was:</strong> " + end1 + "</p>")
        self.response.write(OTHER_PAGE2)
        s = Shift(employee=employee1, start=start1, end=end1)
        s.put()
        key = s.key()
        x = Get(key)
        self.response.write(x)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/shift', ShiftHandler),
    ('/info', InfoHandler),
], debug=True)
