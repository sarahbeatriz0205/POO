from models.Cliente import Cliente, ClienteDAO

class UI:     
    def menu():
        print("1-Inserir, \n2-Listar, \n3-Atualizar, \n4-Excluir, \n5-Fim")
        return int(input("Informe uma opção: "))           
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
    def inserir():
        id = 0
        nome = input("Informe o nome: ")
        email = input("Informe seu e-mail: ")
        telefone = input("Informe seu número de telefone: ")
        c = Cliente(id, nome, email, telefone)
        ClienteDAO().inserir(c)
    def listar():
        c = ClienteDAO.listar()
        print(c)        
    def atualizar():
        UI.listar()
        id = int(input("Informe o id que você quer atualizar: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        telefone = input("Informe o novo telefone: ")

    def excluir():
        UI.listar()
        id = int(input("Informe o id que você quer excluir: "))   
        nome = None 
        email = None 
        telefone = None

UI.main()
# pegar a UI usada na aula