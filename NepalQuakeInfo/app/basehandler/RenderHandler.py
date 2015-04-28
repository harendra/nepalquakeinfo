# -*- coding: utf-8 -*-
'''
Created on Feb 17, 2012

@author: harendra
'''
import webapp2
from webapp2_extras import jinja2

class RenderHandler(object):
    '''
    classdocs
    '''
    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)
    

    def render_response(self, _template, **context):
        j=jinja2.get_jinja2(app=self.app)
        # Renders a template and writes the result to the response.
        self.response.write(j.render_template(_template, **context))  
        