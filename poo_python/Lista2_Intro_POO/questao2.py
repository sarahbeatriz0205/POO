class Viagem:
    def __init__(self):
        self.distancia = 0
        self.tempo = 0
    def velocidade_media(self):
        vm = self.distancia / self.tempo
        return vm

x = Viagem()
x.distancia = float(input("Digite a distância do início até o destino final: "))
x.tempo = float(input("Digite o tempo da viagem: "))
print("Ok! A velocidade média é de", x.velocidade_media(), "km/h")