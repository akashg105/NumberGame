'''
Created on Mar 29, 2016

@author: akash.gupta17
'''
import cherrypy
import os


from shuffleCherry import Practice
#from initialCherry import Practice2
from initialCherry import Practice2
class HelloWorld:
    
    @cherrypy.expose
    def index(self):
        return open("cardCherry.html").read()
    @cherrypy.tools.allow(methods=['POST','GET'])
    def first(self,temp):
       
        #return  my().h(temp,HelloWorld.__sum)
        return Practice().shuffle(temp)
    first.exposed=True
    def second(self):
        return Practice2().initial()
    second.exposed=True

    
cherrypy.config.update({'server.socket_port': 8080})
cherrypy.quickstart(HelloWorld());
    