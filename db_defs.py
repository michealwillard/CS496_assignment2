#  Assignment2
#  Micheal Willard

from google.appengine.ext import ndb
from google.appengine.ext import blobstore

class Message(ndb.Model):
    channel = ndb.StringProperty(required=True)
    date_time = ndb.DateTimeProperty(required=True)
    count = ndb.IntegerProperty(required=True)

class Game(ndb.Model):
    opp = ndb.StringProperty(required=True)
    field = ndb.StringProperty(required=True)
    players = ndb.KeyProperty(repeated=True)
    home_away = ndb.StringProperty(required=True)
    date = ndb.StringProperty(required=True)
    # date = ndb.DateProperty(required=True)
    time = ndb.StringProperty(required=True)
    # time = ndb.TimeProperty(required=True)
    active = ndb.BooleanProperty(required=True)

class GamePlayer(ndb.Model):
    name = ndb.StringProperty(required=True)

class Opponent(ndb.Model):
    name = ndb.StringProperty(required=True)
