# Micheal Willard
# Assignment 2

import webapp2
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers
from google.appengine.ext import ndb
import db_defs

class EditGame(blobstore_handlers.BlobstoreUploadHandler):
    def post(self):
        game_key = ndb.Key(urlsafe=self.request.get('key'))
        game = game_key.get()
        if self.request.get('h_a-action') == 'home':
            game.home_away = "home"
        elif self.request.get('h_a-action') == 'away':
            game.home_away = "away"

        game.opp = self.request.get('opponent-name')
        game.field = self.request.get('field-name')
        game.date = self.request.get('game-date')
        game.time = self.request.get('game-time')
        game.players = [ndb.Key(urlsafe=x) for x in self.request.get_all('players[]')]

        game.put()
        self.redirect('/edit?key=' + game_key.urlsafe() + '&type=game')
