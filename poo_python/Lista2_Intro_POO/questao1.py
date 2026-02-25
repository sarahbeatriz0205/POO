class Circulo:
    def __init__(self):
        self.raio = 0
    def area(self):
        a = 3.14 * (self.raio * self.raio)
        return a
    def circunferencia(self):
        c = 2 * 3.14 * self.raio
        return c

x = Circulo()
x.raio = float(input("Digite o valor do raio: "))
print("Legal! Com essa informação, a área do seu círculo é", x.area(), "e a circuferência é", x.circunferencia())