from datetime import datetime
from pessoa import Pessoa, PessoaDAO
from corrida import Corridas, CorridasDAO

class UI:
    def menu():
        print("1 - Inserir pessoa", "\n2 - Listar pessoas", "\n3 - Pesquisar pelo nome")
        print()
        print("4 - Inserir nova corrida", "\n5 - Listar minhas corridas", "\n6 - Encontrar corrida com menor pace")
        print()
        print("7 - Fim")

        return int(input("Informe uma opção: "))

    def main():
        opcao = 0
        while opcao != 7:
            opcao = UI.menu()
            if opcao == 1: UI.pessoa_inserir()
            if opcao == 2: UI.pessoa_listar()
            if opcao == 3: UI.pessoa_pesquisar()
            if opcao == 4: UI.corrida_inserir()
            if opcao == 5: UI.corrida_listar()
            if opcao == 6: UI.corrida_menorPace()
            if opcao == 7: exit("Nunca deixe de fazer exercícios :)")
    
    def pessoa_inserir():
        idPessoa = 0
        nome = input("Nome: ")
        nascimento = input("Data de nascimento no formato - year-month-day - : ")
        insira = Pessoa(idPessoa, nome, nascimento)
        PessoaDAO.inserir(insira)
    def pessoa_listar():
        for objeto in PessoaDAO.listar():
            print(objeto)
    def pessoa_pesquisar():
        nome = input("Insira o nome que você deseja: ")
        for n in PessoaDAO.listar():
            if n == nome:
                print(n)
    def corrida_inserir():
        idTreino = 0
        data = datetime.now()
        idPessoa = int(input("Insira seu id: "))
        distancia = int("Quantos km você correu? -> ")
        tempo = input("Seu tempo: ")
        tempo = datetime.fromisoformat(tempo)
        tempo = datetime.timedelta(tempo)
        insira = Corridas(idTreino, idPessoa, distancia, tempo)
        CorridasDAO.inserir(insira)
    def corrida_listar():
        for objeto in CorridasDAO.listar():
            print(objeto)
    def corrida_menorPace():
        for objeto in CorridasDAO.listar_menorPace():
            print(objeto)

UI.main()