#classe: a ideia de um objeto, de como ele será, uma abstração. define um tipo de objeto
#Entidade
class Triangulo:
    def __init__(self): #obrigatório; é o construtor: inicialização do objeto
        self.base = 0
        self.altura = 0
    def calc_area(self):
        return self.base * self.altura / 2

#Interface com o usuário   
x = Triangulo()
x.base = float(input("Valor da base: "))
x.altura = float(input("Valor da altura: "))
print("Área: ", x.calc_area())

#variável: nome de referência de um espaço de memória
#instância: objeto criado a partir de uma classe