import cherrypy
import requests

class FacadeService(object):

    def callListar():
        print("chamando listagem")

    def callIncluir(aParametros):
        print("chamando inclusão")

    def callExcluir(aParametros):
        print("chamando exclusão")

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def process(self, iAcao, aParametros):
        return "Hello World"
    
if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(FacadeService())