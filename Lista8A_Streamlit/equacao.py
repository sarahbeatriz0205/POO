import math

class EquacaoGrauDois:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if a == 0: 
            raise ValueError("O valor deve ser maior que 0, senão não é uma equação de 2° grau")

    def calc_delta(self):
        return (self.b**2) - (4 * self.a * self.c)
    
    def x1(self):
        delta = math.sqrt(self.calc_delta()) # raiz quadrada de delta
        return ((-self.b) + delta) // (2 * self.a) # -self.b nega o valor. se self.b for igual a 5, passará a ser -5
    
    def x2(self):
        delta = math.sqrt(self.calc_delta())
        return ((-self.b) - delta) // (2 * self.a)
    
    def ponto_inflexao(self):
        return -self.b / (2 * self.a)
    
    def y(self, x):
        return (self.a * x * x) + (self.b*x) + self.c

    def __str__(self):
        return f"A = {self.a} \nB = {self.b} \nC = {self.c}"