import math
class Retangulo:
    def __init__(self, base, altura):
        # Validação inicial no construtor
        if base >= 0: 
            self.__base = float(base)
        else:
            raise ValueError()
        if altura >= 0:
            self.__altura = float(altura)
        else:
            raise ValueError()
        
    def set_base(self, base):
        if base >= 0:
            self.__base = base
        else:
            raise ValueError()
    def set_altura(self, altura):
        if altura >= 0:
            self.__altura = altura
        else:
            raise ValueError()
        
    def get_base(self):
        return self.__base
    def get_altura(self):
        return self.__altura

    def area(self):
        return self.__base * self.__altura
    def diagonal(self):
        d = (self.__base * self.__base) + (self.__altura * self.__altura)
        d = math.sqrt(d)
        return d
    
    def __str__(self):
        return f"Base: {self.__base:.2f} e Altura: {self.__altura:.2f}"