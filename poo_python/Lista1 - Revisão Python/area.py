class Triangulo:
    def __init__(self): #construtor: inicialização do objeto
        self.b = 0
        self.h = 0
    def calc_area(self):
        return self.b * self.h / 2

x = Triangulo()
x.b = float(input("Base: "))
x.h = float(input("Altura: "))
print("Área: ", x.calc_area())