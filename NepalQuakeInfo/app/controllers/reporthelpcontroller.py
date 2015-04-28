'''
Created on Apr 28, 2015

@author: harendra
'''
from basehandler.BaseHandler import BaseHandler

class HelpReportRequestAdder(BaseHandler):
    
    def post(self):
        pass
    
    def get(self):
        context={}
        self.render_response("addnewhelpreport.html",**context)

class HelpReportRequestGetter(BaseHandler):
    
    def post(self):
        pass
    
    def get(self):
        pass


