class Frete:
    def __init__(self, d, p):
        if d >= 0:
            self.__distanciaTrajeto = float(d)
        else:
            raise ValueError()
        if p >= 0:
            self.__peso = float(p)
        else:
            raise ValueError()
        
    def set_distanciaTrajeto(self, d):
        if d >= 0:
            self.__distanciaTrajeto = d
        else:
            raise ValueError()
    def set_peso(self, p):
        if p >= 0:
            self.__peso = p
        else:
            raise ValueError()
    
    def get_distanciaTrajeto(self):
        return self.__distanciaTrajeto
    def get_peso(self):
        return self.__peso

    def calcFrete(self):
        return self.__distanciaTrajeto * self.__peso

    def __str__(self):
        return f"Distância: {self.__distanciaTrajeto:.2f} \nPeso: {self.__peso:.2f}"

x = Frete(40.5, 20)
print(x)