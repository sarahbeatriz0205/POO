class Frete:
    def __init__(self, distancia, peso):
        self.__distancia = distancia
        self.__peso = peso
    def get_peso(self):
        return self.__peso
    def get_distancia(self):
        return self.__distancia
    def ValorFrete(self):
        return self.__distancia * (self.get_peso() * 0.01)
    def __str__(self):
        return f"Peso = R$ {self.get_peso()} \nDistância = {self.get_distancia()} km \nValor do frete = R$ {self.ValorFrete():.2f}"
    
class FreteExpresso(Frete):
    def __init__(self, distancia, peso, seguro):
        super().__init__(distancia, peso)
        self.__seguro = seguro
    def ValorFrete(self):
        return (self.get_distancia() * self.get_peso()) * 2 + (self.__seguro / 100) # dobro do frete + 1% do seguro
    def __str__(self):
        return super().__str__()