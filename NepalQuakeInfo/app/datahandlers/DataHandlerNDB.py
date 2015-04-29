# -*- coding: utf-8 -*-
'''

@author: harendra
'''
import logging
import json
import datetime
from google.appengine.ext import ndb
from utils.OutputVerifier import OutputVerifier
class DataHandlerNDB():
    def getEntity(self,entityclass,entid,parentclass=None,parentobjectkey=None,create=False):
        if parentobjectkey==None:
            entity=entityclass.get_by_id(entid)
        elif parentobjectkey!=None:
            parentkey=ndb.Key(parentclass,parentobjectkey)
            entity=entityclass.get_by_id(id=entid,parent=parentkey)
        if entity==None and create==True:
            if parentobjectkey==None:
                entity=entityclass(id=entid)
            elif parentobjectkey!=None:
                entity=entityclass(id=entid,parent=parentkey)
        return entity
    
    def getEntityDict(self,entity):
        entityMap={}
        for key in entity._properties:
            try:
                val=getattr(entity,key)
                entityMap[key]=val
            except:
                pass
        verifier=OutputVerifier(entityMap)
        entityMap=verifier.verify()
        return entityMap
        
    
    def getAllEntities(self,entityclass,total=2000,offsetvalue=0,parentclass=None,parentobjectkey=None,filters=None,orderby=None):
        if parentobjectkey==None:
            query=entityclass.query()
        elif parentobjectkey!=None:
            parentkey=ndb.Key(parentclass,parentobjectkey)
            query=entityclass.query(ancestor=parentkey)
        if filters!=None:
            query=self.addFilter(query, filters)
        if orderby!=None:
            query=query.order(orderby)
        return query.fetch(limit=total,offset=offsetvalue)
    
    def getDistinct(self,entityclass,comparentity,propertyname,mainfilter):#mainfilter=filter by userid etc
        offset=0
        fetchedlist=[]
        query=entityclass.query()
        query=self.addFilter(query, mainfilter)
        query=query.order(comparentity)
        while True:
            fetched=query.fetch(offset=offset,limit=1,projection=[comparentity])
            if len(fetched)==1:
                item=fetched[0].to_dict()[propertyname]
                fetchedlist.append(item)
                filtered=query.filter(comparentity==item)
                filtereditems=filtered.fetch(keys_only=True)
                offset+=len(filtereditems)
            else:
                break
        return fetchedlist
    
    def getEntitiesByFilter(self,entityclass,filters,total=2000,offsetvalue=0,orderby=None):
        query=entityclass.query()
        query=self.addFilter(query, filters)
        if orderby!=None:
            query=query.order(orderby)
        return query.fetch(limit=total,offset=offsetvalue)
    
    def getAllKeyEntries(self,entityclass,total=2000,offsetvalue=0,parentclass=None,parentobjectkey=None,filters=None,orderby=None):
        if parentobjectkey==None:
            query=entityclass.query()
        elif parentobjectkey!=None:
            parentkey=ndb.Key(parentclass,parentobjectkey)
            query=entityclass.query(ancestor=parentkey)
        if filters!=None:
            query=self.addFilter(query, filters)
        if orderby!=None:
            query=query.order(orderby)
        return query.fetch(limit=total,offset=offsetvalue,keys_only=True)
        
    def getAllEntitiesByKey(self,entityclass,total=2000,offsetvalue=0,parentclass=None,parentobjectkey=None,filters=None):
        fetched=[]
        if parentobjectkey==None:
            query=entityclass.query()
        elif parentobjectkey!=None:
            parentkey=ndb.Key(parentclass,parentobjectkey)
            query=entityclass.query(ancestor=parentkey)
        if filters!=None:
            query=self.addFilter(query, filters)
        keys=query.fetch(total,keys_only=True)
        
        for key in keys:
            entity=self.getEntity(entityclass,key.string_id(),parentclass,parentobjectkey)
            if entity!=None:
                fetched.append(entity)            
        return fetched
    
    def addFilter(self,query,filters):
        logging.error(filters)
        for curfilter in filters:
            currentfilter=curfilter[0]
            operatorstring=curfilter[1]
            value=curfilter[2]
            if operatorstring=='==':
                query=query.filter(currentfilter == value)
            elif operatorstring=='>':
                query=query.filter(currentfilter > value)
            elif operatorstring=='>=':
                query=query.filter(currentfilter >= value)
            elif operatorstring=='<=':
                query=query.filter(currentfilter <= value)
            elif operatorstring=='<':
                query=query.filter(currentfilter < value)
            elif operatorstring=='!=':
                query=query.filter(currentfilter!=value)
                query=query.order(currentfilter)
        return query
    
    def getEntityID(self,entity):
        return entity.key.id()
    
    def getEntryByKey(self,keyentry):
        return keyentry.get()        
    
    def writeToDataStore(self,entity):
        entity.put()
    
    def deleteEntry(self,entity):
        entity.key.delete()
        

class GenericHandler(object):
    def __init__(self,object_type,data=None,objectid=None,entity=None):
        self.object_type=object_type
        self.handlerndb=DataHandlerNDB()
        if data!=None:
            self.data=data
        if entity!=None:
            self.entity=entity
            logging.error(entity)
            self.data=self.handlerndb.getEntityDict(self.entity)
        if objectid!=None:
            entity=self.handlerndb.getEntity(self.object_type, objectid,create=True)
            self.data=self.handlerndb.getEntityDict(entity)
        logging.error(entity)
        self.entity=entity
    
    def search_entities(self,object_type,filter=None,orderby=None,offset=None,total=None):
        handlerndb=DataHandlerNDB()
        entities=handlerndb.getAllEntities(object_type, total=total, offsetvalue=offset,filters=filter, orderby=orderby)
        return entities
        
    def search(self,object_type,filter=None,orderby=None,offset=None,total=None):
        handlerndb=DataHandlerNDB()
        entities=handlerndb.getAllEntities(object_type, total=total, offsetvalue=offset,filters=filter, orderby=orderby)
        serializedEntities=[]
        for entity in entities:
            objectid=handlerndb.getEntityID(entity)
            serializeddict=handlerndb.getEntityDict(entity)
            serializeddict["objectid"]=objectid
            serializedEntities.append(serializeddict)
        return serializedEntities

    def persist(self):
        self.handlerndb.writeToDataStore(self.entity)
    
    def getValue(self,datakey):
        if self.data.has_key(datakey):
            return self.data[datakey]
        else:
            return None
            
    def setValue(self,entitykey,entityvalue):
        logging.error(entitykey)
        logging.error(entityvalue)
        entitykey=entityvalue
    
    def setValues(self,data):
        if data!=None:
            data_keys=data.keys()
            entdict=self.entity.__dict__
            for key in data_keys:
                if key in entdict:
                    self.entity.__dict__[key]=data[key]
            self.persist()
    
    def update_entity(self,data):
        for field_name in dir(self.entity):
            try:
                setattr(self.entity,field_name,data[field_name])
            except:
                pass
        self.persist()
    
    def addToList(self,entitykey,entityvalue,pickled=False):
        if not pickled:
            entitykey.append(entityvalue)
        else:
            val={"id":entityvalue,"date":datetime.datetime.now()}
            verifier=OutputVerifier(val)
            val=json.dumps(verifier.verify())
            entitykey.append(val)
            
    def deleteEntity(self):
        self.handlerndb.deleteEntry(self.entity)
