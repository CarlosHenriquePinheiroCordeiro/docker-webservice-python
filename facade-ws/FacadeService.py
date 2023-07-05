import cherrypy
import requests
import json

class FacadeService(object):

    def callListar(self, aParametros):
        "Chama o WS de listagem"
        return requests.get("http://persistencia:8080/listar").content

    def callIncluir(self, aParametros):
        "Chama o WS de inclusão, de acordo com os parâmetros informados"
        sSucesso = 'False'
        if self.callValidacaoContato(aParametros["sTipo"], aParametros["sDescricao"]):
            sSucesso = requests.get("http://persistencia:8080/processaInclusao?sNome="+str(aParametros["sNome"])+"&sDescricao="+str(aParametros["sDescricao"])).content
        return sSucesso

    def callValidacaoContato(self, iTipo, sContato):
        "Chama o WS de validação, permitindo ou não a exclusão do contato"
        bRetorno  = True
        sResposta = str(requests.get("http://bo:8080/validaContato?sTipo="+str(iTipo)+"&sContato="+sContato).content).replace('b', '').replace("'", '')
        if sResposta == 'False':
            bRetorno = False
        return bRetorno

    def callExcluir(self, aParametros):
        "Chama o WS de exclusão, de acordo com os parâmetros informados"
        return requests.get("http://persistencia:8080/processaExclusao?sId="+str(aParametros["sId"])).content

    @cherrypy.expose
    def process(self, sAcao, sParametros):
        "Processa a ação desejada através dos parâmetros"
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