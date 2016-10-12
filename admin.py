# Assignment2
# Micheal Willard

import webapp2
import base_page
from google.appengine.ext import ndb
import db_defs

class Admin(base_page.BaseHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}

    def render(self, page):
        self.template_values['games'] = [{'home_away':x.home_away,'opp':x.opp, 'date':x.date, 'time':x.time, 'field':x.field, 'key':x.key.urlsafe()} for x in db_defs.Game.query(ancestor=ndb.Key(db_defs.Game, self.app.config.get('default-group'))).fetch()]
        self.template_values['players'] = [{'name':x.name, 'key':x.key.urlsafe()} for x in db_defs.GamePlayer.query(ancestor=ndb.Key(db_defs.GamePlayer, self.app.config.get('default-group'))).fetch()]
        base_page.BaseHandler.render(self, page, self.template_values)

    def get(self):
        self.render('admin.html')
    #, icon_key=None
    def post(self):
        action = self.request.get('action')
        if action == 'add_game':
            #key: type + id
            k = ndb.Key(db_defs.Game, self.app.config.get('default-group'))
            game = db_defs.Game(parent=k)
            game.opp = self.request.get('opponent-name')
            game.field = self.request.get('field-name')
            game.home_away = self.request.get('home-away')
            game.date = self.request.get('game-date')
            game.time = self.request.get('game-time')
            game.players = [ndb.Key(urlsafe=x) for x in self.request.get_all('players[]')]
            game.active = True
            # put saves, returns to key
            game.put()
            self.template_values['message'] = 'Added the game on ' + game.date + ' to the database.'
        elif action == 'add_player':
            k = ndb.Key(db_defs.GamePlayer, self.app.config.get('default-group'))
            c = db_defs.GamePlayer(parent=k)
            c.name = self.request.get('player-name')
            c.put()
            self.template_values['message'] = 'Added ' + c.name + ' to the database.'
        else:
            self.template_values['message'] = 'Action ' + action + ' is unknown.'
        self.render('admin.html')
