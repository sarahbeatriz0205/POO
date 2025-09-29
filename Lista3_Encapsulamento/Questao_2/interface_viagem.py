from viagem import Viagem
class Interface:
    @staticmethod
    def main():
        distancia = int(input("Insira a distância: "))
        tempo = int(input("Insira o tempo: "))
        x = Viagem(distancia, tempo)
        print("A velocidade média é:", "{:.0f}".format(x.velocidade_media(distancia, tempo)))

Interface.main()