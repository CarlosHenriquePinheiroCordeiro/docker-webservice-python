import cherrypy
import json
from pymongo import MongoClient

class PersistenciaContatoService(object):

    CnxI    = None
    CnxII   = None
    CnxIII  = None
    arquivo = "contatos.txt"

    def getJsonDados(self, iId, sNome, sDescricao):
        #Retorna um JSON a partir dos dados informados do contato
        return {"id":iId,"nome":sNome, "descricao":sDescricao}

    def getTxt(self, sModo = "a"):
        #Retorna o arquivo TXT dos contatos
        oTxt = open(self.arquivo, "a")
        oTxt.close()
        return open(self.arquivo, sModo)
    
    def getContentTxt(self):
        #Retorna o conteúdo do TXT
        oTxt     = self.getTxt("r")
        sContent = oTxt.read()
        oTxt.close()
        return sContent
    
    def getNovoIdContato(self):
        #Retorna o ID para um novo contato com base no último ID inserido
        content = self.getContentTxt()
        id      = 0
        if content != '':
            id = len(self.getTxt("r").readlines())
        return id+1
    
    def getCnxI(self):
        #Retorna a conexão com a instância I do banco
        if self.CnxI is None:
            try:
                self.CnxI = MongoClient("localhost", 8085)
            except:
                None
        return self.CnxI
        
    def getCnxII(self):
        #Retorna a conexão com a instância II do banco
        if self.CnxII is None:
            try:
                self.CnxII = MongoClient("localhost", 8086)
            except:
                None
        return self.CnxII
        
    def getCnxIII(self):
        #Retorna a conexão com a instância III do banco
        if self.CnxIII is None:
            try:
                self.CnxIII = MongoClient("localhost", 8087)
            except:
                None
        return self.CnxIII

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def listar(self):
        "Lista os registros vindos do TXT"
        return self.getContentTxt()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def processaInclusao(self, sNome, sDescricao):
        "Processa a inclusão de um novo contato"
        iId      = self.getNovoIdContato()
        bSucesso = False
        bSucesso = self.incluiContatoTxt  (iId, sNome, sDescricao)    or bSucesso
        bSucesso = self.processaInclusaoBanco(iId, sNome, sDescricao) or bSucesso
        return bSucesso

    def incluiContatoTxt(self, iId, sNome, sDescricao):
        #inclui o novo contato no arquivo txt
        bRetorno = True
        try:
            oTxt = self.getTxt()
            oTxt.write(str(self.getJsonDados(iId, sNome, sDescricao))+"\n")
            oTxt.close()
        except:
            bRetorno = False
        return bRetorno

    def incluiContatoBanco(self, oConexao, iId, sNome, sDescricao):
        #Inclui o novo contato no banco da conexão informada
        bSucesso = False
        if oConexao is not None:
            try:
                oConexao.get_database("contatos").get_collection("contatos").insert_one(self.getJsonDados(iId, sNome, sDescricao))
                bSucesso = True
            except:
                bSucesso = False
        
        return bSucesso

    def processaInclusaoBanco(self, iId, sNome, sDescricao):
        #Processa a inclusão nas três instâncias do mongodb
        bSucesso = False
        bSucesso = bSucesso or self.incluiContatoBanco(self.getCnxI() , iId, sNome, sDescricao)
        #bSucesso = bSucesso or self.incluiContatoBanco(self.getCnxII() , iId, sNome, sDescricao)
        #bSucesso = bSucesso or self.incluiContatoBanco(self.getCnxIII(), iId, sNome, sDescricao)
        return bSucesso

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