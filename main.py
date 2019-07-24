# the import section
import webapp2
import jinja2
import os

# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section
class MapHandler(webapp2.RequestHandler):
	def get(self):
		map_template = the_jinja_env.get_template('Templates/gyms.html')
		self.response.write(map_template.render())

class MainHandler(webapp2.RequestHandler):
  	def get(self):  # for a get request
		welcome_template = the_jinja_env.get_template('Templates/home.html')
		self.response.write(welcome_template.render())   # the responseb687dd05955f68251806cdab733489c7f0a9d898


# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/gyms.html', MapHandler),
  ], debug=True)