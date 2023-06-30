import cherrypy
import requests
import json

class FacadeService(object):

    def callListar(self, aParametros):
        #Chama o WS de listagem
        return requests.get("http://localhost:8083/listar").content

    def callIncluir(self, aParametros):
        #Chama o WS de inclusão, de acordo com os parâmetros informados
        print("chamando inclusão")

    def callExcluir(self, aParametros):
        #Chama o WS de exclusão, de acordo com os parâmetros informados
        print("chamando exclusão")

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def process(self, sAcao, sParametros):
        aProcessos = [
            self.callListar,
            self.callIncluir,
            self.callExcluir
        ]
        return aProcessos[int(sAcao)-1](json.loads(sParametros))
    
if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(FacadeService())