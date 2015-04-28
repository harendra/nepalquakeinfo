# -*- coding: utf-8 -*-
'''

@author: harendra
'''
#check null and verify dates, handle keyvalue pair and list
import datetime
import time
from keys import *
import json
import logging

class OutputVerifier:
    def __init__(self,outputobj=None):
        self.outputobj=outputobj
        self.milliseckey="millisec"
    
    def verify(self):
        if self.outputobj==None:
            return ""
        self.parseObjects(self.outputobj,None,None)
        return self.outputobj
    
    def getEpoch(self,dt):
        epoch=datetime.datetime.utcfromtimestamp(0)
        delta=dt-epoch
        return delta.total_seconds()*1000
    
    def parseObjects(self,outputobj,parent,key):
        if type(outputobj)!=dict and type(outputobj)!=list:
            if type(outputobj)==datetime.datetime:
                parent[key]=str(outputobj.date())#key will be used as index value for lists
                try:
                    parent[self.milliseckey]=self.getEpoch(outputobj)
                except Exception,e:
                    logging.error(e)
            elif type(outputobj)==datetime.date:
                parent[key]=str(outputobj)#key will be used as index value for lists
            elif outputobj==None:
                #parent[key]="" 
                pass
            #logging.error(outputobj)
            #logging.error(type(outputobj))              
            return
        elif type(outputobj)==dict:
            keys=outputobj.keys()
            for key in keys:
                val=outputobj[key]
                self.parseObjects(val,outputobj,key)
        elif type(outputobj)==list:
            for i in range(len(outputobj)):
                val=outputobj[i]
                self.parseObjects(val,outputobj,i)


        