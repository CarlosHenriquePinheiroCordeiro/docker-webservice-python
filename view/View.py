class View:

    def menuAcao(self):
        print("##############################################################################################################")
        print("Contatos")
        print("##############################################################################################################")
        print("Informe a ação desejada:")
        print("1. Listar contatos.")
        print("2. Incluir contato.")
        print("3. Excluir contato.")
        print("4. Encerrar programa.")
        return int(input("Digite aqui: "))
    
    def listar(self):
        return "Listando"
    
    def incluir(self):
        return "Incluindo"
    
    def excluir(self):
        return "Excluindo"