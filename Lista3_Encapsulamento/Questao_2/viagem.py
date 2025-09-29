class Viagem:
    def __init__(self, distancia, tempo):
        self.set_distancia(distancia)
        self.set_tempo(tempo)
    def get_distancia(self):
        return self.__distancia
    def get_tempo(self):
        return self.__tempo
    def set_distancia(self, distancia):
        self.__distancia = distancia
    def set_tempo(self, tempo):
        self.__tempo = tempo

    def velocidade_media(self, distancia, tempo):
        return self.__distancia / self.__tempo