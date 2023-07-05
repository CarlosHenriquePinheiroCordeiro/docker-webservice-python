import json

class View:

    def menuAcao(self):
        "Printa o menu principal de ações para o usuário"
        print("##############################################################################################################")
        print("Contatos")
        print("##############################################################################################################")
        print("Informe a ação desejada:")
        print("1. Listar contatos.")
        print("2. Incluir contato.")
        print("3. Excluir contato.")
        print("4. Encerrar programa.")
        return int(input("Digite aqui: "))
    
    def listar(self, aContatos):
        "Printa a listagem de contatos"
        print("--------------------------------------------------------------------------------------------------------------")
        print("Listando contatos:")
        print("--------------------------------------------------------------------------------------------------------------")
        for sContato in aContatos:
                if sContato != '' and sContato != "'":
                    oContato = json.loads(sContato)
                    print("ID: "+str(oContato['id'])+" ; Nome: "+str(oContato['nome'])+" ; Descrição: "+str(oContato['descricao']))
    
    def incluir(self):
        "Printa o processo interativo da inclusão de contato"
        aTipo = ["Telefone", "Celular", "Email", "Site"]
        print("--------------------------------------------------------------------------------------------------------------")
        sNome = input("Informe o nome do contato: ")
        print("--------------------------------------------------------------------------------------------------------------")
        print("Informe o tipo de contato que deseja incluir:")
        print("1. Telefone - Exemplo: 4735331472")
        print("2. Celular  - Exemplo: 47988114321")
        print("3. Email    - Exemplo: teste@gmail.com")
        print("4. Site     - Exemplo: site.com.br")
        iTipo = int(input("Tipo: "))
        print("--------------------------------------------------------------------------------------------------------------")
        sDescricao = input("Informe o "+aTipo[iTipo-1]+": ")
        print("--------------------------------------------------------------------------------------------------------------")
        return '{"sNome":"'+sNome+'", "sTipo":"'+str(iTipo)+'", "sDescricao":"'+sDescricao+'"}'
    
    def excluir(self):
        "Printa o processo interativo de exclusão do contato"
        return '{"sId":"'+str(input("Informe o ID que deseja excluir o contato"))+'"}'
    
    def mensagemIncluir(self, sSucesso):
        "Printa o resultado da inclusão"
        sMensagem = "Ocorreu um erro durante a inclusão do contato"
        if sSucesso == 'True':
            sMensagem = "Contato incluído com sucesso"
        print(sMensagem)
            
    def mensagemExcluir(self, bSucesso):
        "Printa o resultado da exclusão"
        sMensagem = "Ocorreu um erro durante a exclusão do contato"
        if bSucesso:
            sMensagem = "Contato excluído com sucesso"
        print(sMensagem)