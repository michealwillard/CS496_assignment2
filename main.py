# Assignment2
# Micheal Willard

import webapp2

config = {'default-group':'base-data'}

application = webapp2.WSGIApplication([
    ('/edit/game', 'edit_game.EditGame'),
    ('/edit', 'edit.Edit'),
    ('/admin', 'admin.Admin'),
    ('/', 'home.Home'),
], debug=True, config=config)
