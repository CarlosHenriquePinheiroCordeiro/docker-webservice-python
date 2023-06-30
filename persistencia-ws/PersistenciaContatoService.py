import cherrypy
import json

class PersistenciaContatoService(object):

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def listar(self):
        "Lista os registros vindos do TXT"
        return str(json.loads(open("contatos.txt", "r").read()))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def processaInclusaoNovo(self, sNome, sDescricao):
        "Processa a inclusão de um novo contato"
        return "Hello World"

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def processaInclusaoExistente(self, iId, sDescricao):
        "Adiciona um contato a um já existente, através do ID"
        return "Hello World"

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def processaExclusaoContato(self, sNome, iIdContato):
        "Processa a exclusão de um único contato"
        return "Hello World"

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def processaExclusaoTotalContato(self, sNome, iIdContato):
        "Processa a exclusão total de um contato, excluindo-o totalmente através do ID"
        return "Hello World"
    
if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(PersistenciaContatoService())