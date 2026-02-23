import math

class Circulo:
    def __init__(self, raio):
        self.set_raio(raio)
    def get_raio(self):
        return self.__raio
    def set_raio(self, raio):
        self.__raio = raio
    
    def area(self):
        return math.pi * (self.__raio * self.__raio)
    def circunferencia(self):
        return 2 * math.pi * self.__raio