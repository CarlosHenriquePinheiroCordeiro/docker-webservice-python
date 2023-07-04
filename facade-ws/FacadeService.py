import cherrypy
import requests
import json

class FacadeService(object):

    def callListar(self, aParametros):
        "Chama o WS de listagem"
        return requests.get("http://localhost:8084/listar").content

    def callIncluir(self, aParametros):
        "Chama o WS de inclusão, de acordo com os parâmetros informados"
        sSucesso = 'False'
        if self.callValidacaoContato(aParametros["sTipo"], aParametros[["sDescricao"]]):
            sSucesso = requests.get("http://localhost:8084/processaInclusao?sNome="+str(aParametros["sNome"])+"&sDescricao="+str(aParametros["sDescricao"])).content
        return sSucesso

    def callValidacaoContato(self, iTipo, sContato):
        "Chama o WS de validação, permitindo ou não a exclusão do contato"
        bRetorno  = True
        sResposta = str(requests.get("http://localhost:8086/validaContato?sTipo="+str(iTipo)+"&sContato="+sContato).content).replace('b', '').replace("'", '')
        if sResposta == 'False':
            bRetorno = False
        return bRetorno

    def callExcluir(self, aParametros):
        "Chama o WS de exclusão, de acordo com os parâmetros informados"
        return requests.get("http://localhost:8084/processaExclusao?sId="+str(aParametros["sId"])).content

    @cherrypy.expose
    def process(self, sAcao, sParametros):
        aProcessos = [
            self.callListar,
            self.callIncluir,
            self.callExcluir
        ]
        return aProcessos[int(sAcao)-1](json.loads(sParametros))
    
if __name__ == '__main__':
    config = {'server.socket_host': '127.0.0.1', 'server.socket_port':8082}
    cherrypy.config.update(config)
    cherrypy.quickstart(FacadeService())