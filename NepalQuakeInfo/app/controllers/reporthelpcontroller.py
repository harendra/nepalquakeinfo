'''
Created on Apr 28, 2015

@author: harendra
'''

import logging

from basehandler.BaseHandler import BaseHandler
from datetime import datetime
import uuid
from datahandlers.dao.HelpRequestReportDAO import HelpRequestReportDAO
import json
import jinja2
from model.mainmodels import HelpRequestReport
from utils.OutputVerifier import OutputVerifier

class HelpReportRequestAdder(BaseHandler):
    def post(self):
        result=None
        postparams=self.request.POST
        logging.info(postparams)
        savedata={}
        attributes = [ "reporter_name", "reporter_email", "reporter_phone", "help_type", "help_address", "latitude", "longitude", "details", "imagelink"]
        try:
            for key in attributes:
                savedata[key]=postparams[key].strip()
            if len(postparams["latitude"].strip())!=0 and len(postparams["longitude"].strip())!=0:
                savedata["latitude"]=float(postparams["latitude"].strip())
                savedata["longitude"]=float(postparams["longitude"].strip())
            else:
                savedata["latitude"]=0.0;
                savedata["longitude"]=0.0;      
            savedata["reported_date"]=datetime.now()  
            savedata["status"]="active" #this can be progress and complete    
            new_enity_id=str(uuid.uuid4())
            helpdao=HelpRequestReportDAO(savedata,True,new_enity_id)
            helpdao.write_values()
        except Exception,e:
            logging.exception(e)
            result={"result":"failure"}
        if result==None:
            result={"result":"success"}
        logging.info(result)
        self.response.write(json.dumps(result))
    
    def get(self):
        context={}
        self.render_response("addnewhelpreport.html",**context)
        
class Thanks(BaseHandler):
    def get(self):
        context={}
        self.render_response("reportadded.html",**context)

class HelpReportRequestGetter(BaseHandler):
    
    def post(self):
        getparams=self.request.POST
        pageno=1
        if "pageno" in getparams:
            pageno=int(getparams["pageno"])
        verified_entities=self.getData(pageno)
        result={"result":"success","data":verified_entities}
        self.response.write(result)
    
    def get(self):
        getparams=self.request.GET
        pageno=1
        if "pageno" in getparams:
            pageno=int(getparams["pageno"])
        verified_entities=self.getData(pageno)
        mapdata=[]
        for entity in verified_entities:
            if entity["latitude"]!=0 and entity["longitude"]!=0:
                mapdata.append({"latitude":entity["latitude"],"longitude":entity["longitude"]})
        result={"result":"success","data":verified_entities,"nextpage":pageno+1,"mapdata":json.dumps(mapdata)}
        self.render_response("reportlist.html",**result)
    
    def getData(self,pageno):
        helpdao=HelpRequestReportDAO(None,False,None)
        entities=helpdao.search(HelpRequestReport, offset=(pageno-1)*20, total=20)
        en=OutputVerifier(entities)
        verified_entities=en.verify()
        return verified_entities
        
        
        
            


