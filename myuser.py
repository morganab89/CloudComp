import webapp2
from google.appengine.ext import ndb

class MyUser(ndb.Model):
    # email address of this user
    email_address = ndb.StringProperty()
    users_name = ndb.StringProperty()
    users_age = ndb.IntegerProperty()
