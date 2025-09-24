from ingresso import Ingresso

class InterfaceUsuario: # Não tem instâncias
    @staticmethod # é um método chamado com a classe 
    def main(): # nome "main" para mera organização do código
        op = 0
        while op != 2:
            op  = InterfaceUsuario.menu()
            if op == 1:
                InterfaceUsuario.ingresso()
    @staticmethod
    def menu():
        print("1 - Ingresso \n2 - Fim")
        op = int(input("Escolha uma opção: ")) # Variável local: só existe enquanto a função roda
        return op
    @staticmethod
    def ingresso():
        x = Ingresso() # Ingresso.__init__()
        x.dia = input("Informe o dia desejado: ")
        x.horario = int(input("Informe o horário desejado: "))
        print("Sua sessão será no dia:", x.dia, "às", x.horario)
        print("O valor será de R$:", x.ingresso_inteira())
    
InterfaceUsuario.main()
