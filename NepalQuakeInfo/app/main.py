import webapp2
from urls import routes
from config import config
from webapp2_extras import jinja2
app = webapp2.WSGIApplication(routes=routes, debug=True, config=config)

def handle_404(request,response,exception):
    context={}
    templater=jinja2.get_jinja2(app=app)
    #response.write('The page you were trying to found has moved or does not exist!')
    response.write(templater.render_template('error404.html',**context))
    response.set_status(404)

def handle_500(request,response,exception):
    context={}
    templater=jinja2.get_jinja2(app=app)
    #response.write('The page you were trying to found has moved or does not exist!')
    response.write(templater.render_template('error500.html',**context))
    response.set_status(404)
    
app.error_handlers[404]=handle_404
#app.error_handlers[500]=handle_500