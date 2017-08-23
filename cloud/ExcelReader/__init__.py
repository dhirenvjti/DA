from .handlers import *

app = webapp2.WSGIApplication([
    ('/excel_reader/mu', MUHandler),
])