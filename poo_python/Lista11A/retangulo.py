import math

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def diagonal(self):
        return int(math.sqrt((self.base * self.base) + (self.altura * self.altura)))
    def __str__(self):
        return f"Base (Lado 1) = {self.base} \nAltura (Lado 2) = {self.altura} \nÁrea = {self.area()} \nDiagonal = {self.diagonal()}"

class Quadrado(Retangulo):
    def __init__(self, lado1, lado2):
        super().__init__(lado1, lado2)
        if lado1 != lado2:
            raise ValueError("Não é um quadrado!")
    def area(self):
        return self.base * self.altura
    def diagonal(self):
        return int(self.base * (math.sqrt(2)))
    def __str__(self):
        return super().__str__()