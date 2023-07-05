from view.View import View
import requests

def listar(oView):
    callListar(oView)
    return True

def callListar(oView):
    "Chama o WS de listagem"
    sRetorno = str(requests.get("http://localhost:8080/process?sAcao=1&sParametros={}").content)
    if sRetorno == "b''":
        sRetorno = ''
    sRetorno = sRetorno.replace('b\"{', '{').split('\\n')
    oView.listar(sRetorno)

def incluir(oView):
    "Invoca a chamada do WS de inclusão"
    oView.mensagemIncluir(callIncluir(oView.incluir()))
    return True

def callIncluir(sJsonParametros):
    "Chama o WS de inclusão"
    print("Processando...")
    sSucesso = None
    try:
        sSucesso = requests.get("http://localhost:8080/process?sAcao=2&sParametros="+sJsonParametros).content
    except:
        print("Ocorreu um erro de conexão com o serviço")
        sSucesso = False
    return sSucesso


def excluir(oView):
    "Invoca a chamada do WS de exclusão"
    oView.mensagemExcluir(callExcluir(oView.excluir()))
    return True

def callExcluir(sJsonParametros):
    "Chama o WS de exclusão"
    return requests.get("http://localhost:8080/process?sAcao=3&sParametros="+sJsonParametros).content

def encerrar(oView):
    "Encerra o programa"
    return False

bExecutando = True
oView       = View()
aAcoes      = [
    listar,
    incluir,
    excluir,
    encerrar
]
while bExecutando:
    bExecutando = aAcoes[oView.menuAcao()-1](oView)