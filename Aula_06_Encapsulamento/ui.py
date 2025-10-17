from ingresso import Ingresso
class UI:       # interface com o usuário -  não tem instância
    @staticmethod
    def main(): # método estático é um método chamado com a classe 
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.ingresso()
            if op == 2: UI.viagem()
    @staticmethod
    def menu():
        print("1-Ingresso, 2-Viagem, 3-Fim")
        op = int(input("Escolha uma opção: "))
        return op
    @staticmethod
    def ingresso():
        x = Ingresso()  # Ingresso.__init__()
        #print(x.dia) -----------> esses valores ele só acessa se não tiver encapsulado
        #print(x.hora)
        
        print(x.get_dia()) #get: recebe o valor de certo atributo
        print(x.get_hora())
        x.set_dia = input("Informe o dia [dom, seg, ... sab]: ") #set: altera o valor de um atributo implicitamente com base no get
        x.set_hora = int(input("Informe a hora [0-23]: "))
        print(f"Valor do ingresso R$ {x.inteira():.2f}")
    @staticmethod
    def viagem():
        pass

UI.main() #chamada dessa forma quando é uma classe estática