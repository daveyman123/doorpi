import webapp2
#import sys
#import sys
#sys.path.insert(0, 'libs')
from google.appengine.ext import vendor
#import pexpect
vendor.add('lib')
import pexpect

import bluetooth
import pexpect
class MainHandler(webapp2.RequestHandler):
    def get(self):

        submit = "<input type = 'submit'/>"
        form = "<form method = 'post'>" + submit + "</form>"
        self.response.write(form)
    def post(self):
        bluetooth.connect()
        self.response.write('bye world')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
