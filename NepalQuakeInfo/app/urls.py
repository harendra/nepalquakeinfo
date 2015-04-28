# -*- coding: utf-8 -*-
"""URL definitions."""
import webapp2
from webapp2_extras import routes
routes = [
          (r'/','controllers.maincontroller.HomeController'),
          (r'/addnewhelpreport','controllers.reporthelpcontroller.HelpReportRequestAdder'),  
          ]

'''
    (r'/login','authentication.Authenticator.LoginRedirector'),
    (r'/loginerror','authentication.Authenticator.LoginIncorrectHandler')
'''