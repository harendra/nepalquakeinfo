'''
Created on Apr 28, 2015

@author: harendra
'''

import logging

from basehandler.BaseHandler import BaseHandler
<<<<<<< HEAD
from model.mainmodels import HelpRequestReport
=======
from datetime import datetime
import uuid
from datahandlers.dao.HelpRequestReportDAO import HelpRequestReportDAO
import json
>>>>>>> inputnewhelpreport

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
        result=None
        postparams=self.request.POST
        savedata={}
        try:
            savedata["reporter_name"]=postparams["reporter_name"].strip()
            savedata["reporter_email"]=postparams["reporter_email"].strip()
            savedata["reporter_phone"]=postparams["reporter_phone"].strip()
            savedata["reported_date"]=datetime.now().strip()
            savedata["help_type"]=postparams["help_type"].strip()
            savedata["help_address"]=postparams["help_address"].strip()
            if len(postparams["latitude"].strip())!=0 and len(postparams["longitude"].strip()!=0):
                savedata["latitude"]=float(postparams["latitude"].strip())
                savedata["longitude"]=float(postparams["longitude"].strip())
            else:
                savedata["latitude"]=0;
                savedata["longitude"]=0;
            savedata["details"]=postparams["details"].strip()
            savedata["imagelink"]=postparams["imagelink"].strip()
            
            new_enity_id=uuid.uuid4()
            helpdao=HelpRequestReportDAO(savedata,True,new_enity_id)
            helpdao.write_values()
        except:
            result={"result":"failure"}
        if result!=None:
            result={"result":"success"}
        return json.dumps(result)
    
    def get(self):
        context={}
        self.render_response("addnewhelpreport.html",**context)

class HelpReportRequestGetter(BaseHandler):
    
    def post(self):
        pass
    
    def get(self):
        pass


