from circulo import Circulo

class Interface:
    @staticmethod
    def main():
       raio = int(input("Insira o raio: "))
       x = Circulo(raio)
       print("A área é:", x.area(), "\nA circunferência é:", x.circunferencia())
    
Interface.main()