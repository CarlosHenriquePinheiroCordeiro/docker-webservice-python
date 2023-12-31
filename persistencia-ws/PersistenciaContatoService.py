import cherrypy
import json
import pymongo

class PersistenciaContatoService(object):

    CnxI    = None
    CnxII   = None
    CnxIII  = None
    arquivo = "contatos.txt"

    def getJsonDados(self, iId, sNome, sDescricao):
        "Retorna um JSON a partir dos dados informados do contato"
        return {"id":iId,"nome":sNome, "descricao":sDescricao}

    def getTxt(self, sModo = "a"):
        "Retorna o arquivo TXT dos contatos"
        oTxt = open(self.arquivo, "a")
        oTxt.close()
        return open(self.arquivo, sModo)
    
    def getContentTxt(self):
        "Retorna o conteúdo do TXT"
        oTxt     = self.getTxt("r")
        sContent = oTxt.read()
        oTxt.close()
        return sContent
    
    def getNovoIdContato(self):
        "Retorna o ID para um novo contato com base no último ID inserido"
        content = self.getContentTxt()
        id      = 0
        if content != '':
            aContatos = content.split('\n')
            id = json.loads(aContatos[len(aContatos)-2])['id']
        return str(int(id)+1)
    
    def getCnxI(self):
        "Retorna a conexão com a instância I do banco"
        if self.CnxI is None:
            try:
                self.CnxI = pymongo.MongoClient("mg1", 27017)
            except:
                None
        return self.CnxI
        
    def getCnxII(self):
        "Retorna a conexão com a instância II do banco"
        if self.CnxII is None:
            try:
                self.CnxII = pymongo.MongoClient("mg2", 27017)
            except:
                None
        return self.CnxII
        
    def getCnxIII(self):
        "Retorna a conexão com a instância III do banco"
        if self.CnxIII is None:
            try:
                self.CnxIII = pymongo.MongoClient("mg3", 27017)
            except:
                None
        return self.CnxIII
    
    def getCollectionContatos(self, oConexao):
        "Retorna a collection de Contatos a partir de uma instância de conexão com o MongoDB"
        return oConexao.get_database("contatos").get_collection("contatos")

    @cherrypy.expose
    def listar(self):
        "Lista os registros vindos do TXT"
        return self.getContentTxt()

    @cherrypy.expose
    def processaInclusao(self, sNome, sDescricao):
        "Processa a inclusão de um novo contato"
        iId      = self.getNovoIdContato()
        bSucesso = False
        bSucesso = self.incluiContatoTxt  (iId, sNome, sDescricao)    or bSucesso
        bSucesso = self.processaInclusaoBanco(iId, sNome, sDescricao) or bSucesso
        return str(bSucesso)

    def incluiContatoTxt(self, iId, sNome, sDescricao):
        "Inclui o novo contato no arquivo txt"
        bRetorno = True
        try:
            oTxt = self.getTxt()
            oTxt.write(str(self.getJsonDados(iId, sNome, sDescricao)).replace("'", '"')+"\n")
            oTxt.close()
        except:
            bRetorno = False
        return bRetorno

    def incluiContatoBanco(self, oConexao, iId, sNome, sDescricao):
        "Inclui o novo contato no banco da conexão informada"
        bSucesso = None
        if oConexao is not None:
            try:
                self.getCollectionContatos(oConexao).insert_one(self.getJsonDados(iId, sNome, sDescricao))
                bSucesso = True
            except:
                bSucesso = False
        
        return bSucesso

    def processaInclusaoBanco(self, iId, sNome, sDescricao):
        "Processa a inclusão nas três instâncias do MongoDB"
        bSucesso = False
        bSucesso = self.incluiContatoBanco(self.getCnxI()  , iId, sNome, sDescricao) or bSucesso
        bSucesso = self.incluiContatoBanco(self.getCnxII() , iId, sNome, sDescricao) or bSucesso
        bSucesso = self.incluiContatoBanco(self.getCnxIII(), iId, sNome, sDescricao) or bSucesso
        return bSucesso

    @cherrypy.expose
    def processaExclusao(self, sId):
        "Processa a exclusão completa de um contato"
        bSucesso = False
        bSucesso = self.excluiContatoTxt(int(sId))             or False
        bSucesso = self.processaExclusaoContatoBanco(int(sId)) or False
        return str(bSucesso)
    
    def excluiContatoTxt(self, iId):
        "Executa a exclusão de um contato no TXT através do seu ID"
        sContent = self.getContentTxt().replace("'", '"')
        if sContent != '':
            self.getTxt("w").close()
            oTxt = self.getTxt()
            aContatos = sContent.split('\n')
            for sContato in aContatos:
                if sContato != '' and int(json.loads(sContato)['id']) != iId:
                    oTxt.write(sContato+'\n')
            oTxt.close()
        return True
    
    def processaExclusaoContatoBanco(self, iId):
        "Exclui o contato em todas as três instâncias do banco"
        bSucesso = False
        bSucesso = self.excluiContatoBanco(self.getCnxI()  , iId) or bSucesso
        bSucesso = self.excluiContatoBanco(self.getCnxII() , iId) or bSucesso
        bSucesso = self.excluiContatoBanco(self.getCnxIII(), iId) or bSucesso
        return bSucesso

    def excluiContatoBanco(self, oConexao, iId):
        "Exclusão um contato através do seu ID na instância do banco informada"
        bSucesso = None
        try:
            self.getCollectionContatos(oConexao).delete_one({"id":str(iId)})
            bSucesso = True
        except:
            bSucesso = False
        return bSucesso

if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(PersistenciaContatoService())