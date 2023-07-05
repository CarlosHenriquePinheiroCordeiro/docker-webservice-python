import cherrypy
import re


class BoContatoService(object):

    regTelefone = r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
    regEmail    = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
    regSite     = r'((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*'

    @cherrypy.expose
    def validaContato(self, sTipo, sContato):
        "Retorna o resultado da chamada da validação do contato informado"
        return str(self.verificaContatoInformadoTipo(int(sTipo), sContato))
    
    def verificaContatoInformadoTipo(self, iTipo, sContato):
        "Retorna se o contato informado é válido para ser incluso em banco, a partir do tipo"
        aTipo = [
            self.regTelefone,
            self.regTelefone,
            self.regEmail,
            self.regSite
        ]
        return self.validaRegexContato(sContato, aTipo[iTipo-1])
    
    def validaRegexContato(self, sContato, sRegex):
        "Retorna se o contato informado está de acordo com o regex informado"
        bRetorno = False
        try:
            if re.fullmatch(re.compile(sRegex), sContato):
                bRetorno = True
        except:
            bRetorno = False
        return bRetorno
    
if __name__ == '__main__':
    config = {'server.socket_host': '0.0.0.0'}
    cherrypy.config.update(config)
    cherrypy.quickstart(BoContatoService())