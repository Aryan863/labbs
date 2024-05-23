import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello World. We are at VIT,pune")
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)