# the import section
import webapp2
import jinja2
import os
from google.appengine.api import users
from google.appengine.ext import ndb


# this initializes the jinja2 environment
# this will be the same in every app that uses the jinja2 templating library 
the_jinja_env = jinja2.Environment(
  loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
  extensions=['jinja2.ext.autoescape'],
  autoescape=True)

# other functions should go above the handlers or in a separate file

# the handler section

class CssiUser(ndb.Model):
  first_name = ndb.StringProperty()
  last_name = ndb.StringProperty()
  email = ndb.StringProperty()
  print(first_name)




class MainHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		welcome_template = the_jinja_env.get_template('Templates/home.html')
		self.response.write(welcome_template.render())   # the response
		user = users.get_current_user()
		if user:
			# Create the sign out link (for later use).
			signout_link_html = '<a href="%s">sign out</a>' % (users.create_logout_url('/'))
			# If the user is logged in, get their email address.
			email_address = user.nickname()
			# Then query Datastore to see if a user with this email has registered as
			# a CssiUser before.
			cssi_user = CssiUser.query().filter(CssiUser.email == email_address).get()
			# If the query is successful, the variable will have a user in it, so the
			# following code will run.
			if cssi_user :
				self.response.write('''
					Welcome %s %s (%s)! <br> %s <br>''' % (
						cssi_user.first_name,
						cssi_user.last_name,
						email_address,
						signout_link_html))
			    # the response
				# if the query wasn't successful, the variable will be empty, so this code
				# will run instead.
			else:
        # Registration form for a first-time visitor:
				self.response.write('''
					Welcome to our site, %s!  Please sign up! <br>
					<form method="post" action="/">
					<input type="text" name="first_name">
					<input type="text" name="last_name">
					<input type="submit">
					</form><br> %s <br>
					''' % (email_address, signout_link_html))

		else:
			# If the user isn't logged in...
			login_url = users.create_login_url('/')
			login_html_element = '<a href="%s">Sign in</a>' % login_url
			self.response.write('Please log in.<br>' + login_html_element)
	def post(self):
		user = users.get_current_user()
# Create a new CSSI user.
		cssi_user = CssiUser(
			first_name=self.request.get('first_name'),
			last_name=self.request.get('last_name'),
			email=user.nickname())
# Store that Entity in Datastore.
		cssi_user.put()
		meme_template = the_jinja_env.get_template('Templates/home2.html')
		self.response.write(meme_template.render())
		# profile = {
		# "name": str(cssi_user.first_name)
		# }

		# # Show confirmation to the user. Include a link back to the index.
		# profile_template = the_jinja_env.get_template('Templates/profile.html')
		# self.response.write(profile_template.render())   # the response



class MapHandler(webapp2.RequestHandler):
	def get(self):
		map_template = the_jinja_env.get_template('Templates/gyms.html')
		self.response.write(map_template.render())


class HealthHandler(webapp2.RequestHandler):
	def get(self):
		health_template = the_jinja_env.get_template('Templates/health.html')
		self.response.write(health_template.render())

class RvHandler(webapp2.RequestHandler):
	def get(self):  # for a get request
		rv_template = the_jinja_env.get_template('Templates/resources-videos.html')
		self.response.write(rv_template.render())   # the response

class WorkHandler(webapp2.RequestHandler):
  	def get(self):  # for a get request
		work_template = the_jinja_env.get_template('Templates/workouts.html')
		self.response.write(work_template.render())   # the response

class SecretHandler(webapp2.RequestHandler):
  def get(self):
    user = users.get_current_user()
    if user:
      email_address = user.nickname()
      cssi_user = CssiUser.query().filter(CssiUser.email == email_address).get()
      if cssi_user:
        self.response.write("You found the secret content!")
        return  self.error(403)

    # If either above condition is not met, this line will run instead:
    self.response.write("Sorry, this page is only for CSSI users.")

class QuizHandler(webapp2.RequestHandler):
	def get(self):
		quiz_template = the_jinja_env.get_template('Templates/quiz.html')
		self.response.write(quiz_template.render())   # the response


# the app configuration section	
app = webapp2.WSGIApplication([
  #('/', MainPage),
  ('/', MainHandler),
  ('/gyms.html', MapHandler),
  ('/resources-videos.html', RvHandler),
  ('/workouts.html', WorkHandler),
  ('/health.html', HealthHandler),
  ('/quiz.html', QuizHandler),
  ], debug=True)