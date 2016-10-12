# Assignment2
# Micheal Willard
import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class Home(base_page.BaseHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}

    def render(self, page):
        self.template_values['games'] = [{'home_away':x.home_away,'opp':x.opp, 'date':x.date, 'time':x.time, 'field':x.field, 'key':x.key.urlsafe()} for x in db_defs.Game.query(ancestor=ndb.Key(db_defs.Game, self.app.config.get('default-group'))).fetch()]
        self.template_values['players'] = [{'name':x.name, 'key':x.key.urlsafe()} for x in db_defs.GamePlayer.query(ancestor=ndb.Key(db_defs.GamePlayer, self.app.config.get('default-group'))).fetch()]
        base_page.BaseHandler.render(self, page, self.template_values)

    def get(self):
        self.render('home.html')
