from view.View import View
import requests

def listar(oView):
    print(oView.listar())
    return True

def callListar():
    #chamar WS de listagem
    return []

def incluir(oView):
    aValores = oView.incluir()
    return True

def callIncluir(sNome, iTipo, sContato):
    print("Processando...")
    try:
        #chamar WS de listagem
        requests.get("http://localhost:8082/process?numero=10")
    except:
        print("Ocorreu um erro de conexão com o serviço")


def excluir(oView):
    print(oView.excluir())
    return True

def encerrar(oView):
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