import cherrypy
import requests

class BoContatoService(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def process(self, numero):
        return "Hello World: "+numero
    
#if __name__ == '__main__':
#    config = {'server.socket_host': '0.0.0.0'}
#    cherrypy.config.update(config)
#    cherrypy.quickstart(BoContatoService())

#request = requests.get("http://localhost:8082/process?numero=10")
#print(request.content)