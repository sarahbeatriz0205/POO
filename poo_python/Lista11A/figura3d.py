from abc import ABC, abstractmethod

class FiguraTridimensional(ABC):
    @abstractmethod # não sabe o que ainda irá fazer, mas vai existir
    def get_volume(self): # toda figura tridimensional tem volume
        pass

class Esfera(FiguraTridimensional):
    def __init__(self, raio):
        self.__raio = raio
    def get_raio(self):
        return self.__raio
    def get_volume(self):
        return (4/3) * 3.14 * (self.get_raio() * self.get_raio() * self.get_raio())
    
class Cubo(FiguraTridimensional):
    def __init__(self, lado):
        self.__lado = lado
    def get_lado(self):
        return self.__lado
    def get_volume(self):
        return self.get_lado() * self.get_lado() * self.get_lado()