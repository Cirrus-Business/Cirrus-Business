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

FORM_PAGE =  """ 
<!doctype html>
<html>
  <body>
    <form action="/shift" method="post">
      <div><select name="employees">
         <option value="bob">Bob</option>
         <option value="guy">Pete</option>
         <option value="tim">Tim</option>
         <option value="steve">Steve</option>
         </select>
       </div>
      <div><input type='button'></input>
       </div>
       
      <div><input type="submit" value="Submit"></div>
    </form>
  </body>
</html>

"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
         self.response.write(FORM_PAGE)

class ShiftHandler(webapp2.RequestHandler):
    def post(self):
        self.response.write("")
        
        
        
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/shift', ShiftHandler),
], debug=True)
