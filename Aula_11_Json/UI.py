import ClienteDAO
from ClienteDAO import Cliente

class UI:
    def menu():
        print("1 - Inserir, \n2 - Listar, \n3 - Atualizar, \n4 - Excluir, \n5 - Fechar")
        return int(input("Informe uma opção: "))
    def main():
        opcao = 0
        while opcao != 5:
            opcao = UI.menu()
            if opcao == 1: UI.inserir() 
            if opcao == 2: UI.listar() 
            if opcao == 3: UI.atualizar() 
            if opcao == 4: UI.excluir()
    def inserir():
        id = int(input("Seu ID: "))
        nome = input("Seu nome: ")
        c = Cliente(id, nome)
        ClienteDAO().inserir(c)
    def listar():
        pass
    def atualizar():
        pass
    def excluir():
        pass

UI.main()