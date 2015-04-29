'''
Created on Apr 29, 2015

@author: harendra
'''
from datahandlers.DataHandlerNDB import GenericHandler
from model.mainmodels import HelpRequestReport

class HelpRequestReportDAO(GenericHandler):
    
    def __init__(self, inputdata=None,create=False,objectid=None):
        self.inputdata=inputdata
        self.objectid=objectid
        #check if exists
        super(HelpRequestReportDAO,self).__init__(HelpRequestReport,data=inputdata,objectid=objectid)
    
    def get_data(self):
        return self.entity
    
    def write_values(self):
        self.update_entity(self.inputdata)
        
        
        