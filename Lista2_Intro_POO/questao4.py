class Ingresso: #Entidade: tem instâncias
    def __init__(self):
        self.dia = ""
        self.horario = 0
    def ingresso_inteira(self):
        if self.dia == "qua":
            return 8
        if self.dia in ["seg", "ter", "qui"]:
            valor = 16
        else:
            valor = 20
        if self.hora == 0 or self.hora >= 17:
            valor = valor * 1.5
        return valor
    def meia(self):
        if self.dia == "qua":
            return self.ingresso_inteira() / 2

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

# Métodos especiais (métodos mágicos): métodos com dois underlines no início e no fim de um nome