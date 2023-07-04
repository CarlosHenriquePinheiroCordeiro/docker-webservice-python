from view.View import View
import requests

def listar(oView):
    callListar(oView)
    return True

def callListar(oView):
    "Chama o WS de listagem"
    oView.listar(str(requests.get("http://localhost:8082/process?sAcao=1&sParametros={}").content).replace('"', '').replace('b{', '{').replace("'", '"').split('\\n'))

def incluir(oView):
    "Invoca a chamada do WS de inclusão"
    return oView.mensagemIncluir(callIncluir(oView.incluir()))

def callIncluir(sJsonParametros):
    "Chama o WS de inclusão"
    print("Processando...")
    try:
        requests.get("http://localhost:8082/process?sAcao=2&sParametros="+sJsonParametros)
    except:
        print("Ocorreu um erro de conexão com o serviço")
    return True


def excluir(oView):
    "Invoca a chamada do WS de exclusão"
    oView.mensagemExcluir(callExcluir(oView.excluir()))
    return True

def callExcluir(sJsonParametros):
    "Chama o WS de exclusão"
    requests.get("http://localhost:8082/process?sAcao=3&sParametros="+sJsonParametros)

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