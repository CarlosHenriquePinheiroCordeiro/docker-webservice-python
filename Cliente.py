from view.View import View

def listar(oView):
    print(oView.listar())
    return True

def incluir(oView):
    print(oView.incluir())
    return True

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