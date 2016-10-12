#  Assignment2
#  Micheal Willard
import webapp2
import base_page
from google.appengine.ext import ndb
# from google.appengine.api import images
# from google.appengine.ext import blobstore
import db_defs

class Edit(base_page.BaseHandler):
    def __init__(self, request, response):
        self.initialize(request, response)
        self.template_values = {}
        self.template_values['edit_url'] = '/edit/game'

    # def post(self):
    #     self.render('edit.html')
    # revise from get to post
    def get(self):
        if self.request.get('type') == 'game':
            game_key = ndb.Key(urlsafe=self.request.get('key'))
            game = game_key.get()
            self.template_values['game'] = game
            players = db_defs.GamePlayer.query(ancestor=ndb.Key(db_defs.GamePlayer, self.app.config.get('default-group')))
            player_boxes = []
            for p in players:
                if p.key in game.players:
                    player_boxes.append({'name':p.name, 'key':p.key.urlsafe(), 'checked':True})
                else:
                    player_boxes.append({'name':p.name, 'key':p.key.urlsafe(), 'checked':False})
            self.template_values['players'] = player_boxes
        self.render('edit.html', self.template_values)
