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

class MainHandler(webapp2.RequestHandler):
  	def get(self):  # for a get request
		welcome_template = the_jinja_env.get_template('Templates/home.html')
		self.response.write(welcome_template.render())   # the response

class MapHandler(webapp2.RequestHandler):
	def get(self):
		map_template = the_jinja_env.get_template('Templates/gyms.html')
		self.response.write(map_template.render())

class RvHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		rv_template = the_jinja_env.get_template('Templates/resources-videos.html')
		self.response.write(rv_template.render())   # the response

class WorkHandler(webapp2.RequestHandler):
  	def get(self):  # for a get request
		work_template = the_jinja_env.get_template('Templates/workouts.html')
		self.response.write(work_template.render())   # the response


# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/gyms.html', MapHandler),
  ('/resources-videos.html', RvHandler),
  ('/workouts.html', WorkHandler),
  ], debug=True)