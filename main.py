import webapp2
import bluetooth

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
