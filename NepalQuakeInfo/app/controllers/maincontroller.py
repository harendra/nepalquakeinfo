'''
Created on Apr 28, 2015

@author: harendra
'''
import json
from basehandler.BaseHandler import BaseHandler

class HomeController(BaseHandler):
    
    def get(self):
        data={"hello":"world"}
        self.render_response("index.html",**data)
    
    def post(self):
        data={"hello":"world"}
        self.response.write(json.dumps(data))

        