'''
Created on Apr 28, 2015

@author: harendra
'''

import logging

from basehandler.BaseHandler import BaseHandler
from model.mainmodels import HelpRequestReport

class HelpReportRequestAdder(BaseHandler):

    @classmethod
    def get_canonical_post_data(self,request):
        data = dict()
        for attr in HelpRequestReport.attributes:
            data[attr]=request.get(attr)
        return data

    def post(self):
        post_data = HelpReportRequestAdder.get_canonical_post_data(self.request)
        logging.info(post_data)
        self.render_response("reportadded.html")
    
    def get(self):
        context={}
        self.render_response("addnewhelpreport.html",**context)

class HelpReportRequestGetter(BaseHandler):
    
    def post(self):
        pass
    
    def get(self):
        pass


