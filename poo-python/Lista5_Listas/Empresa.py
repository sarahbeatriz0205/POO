class Cliente:
    def __init__(self, nome, limite):
        self.set_nome(nome)
        self.set_limite(limite)
        self.__socio = None
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome
    def get_limite(self):
        return self.__limite
    def get_limite_sociedade(self):
        if self.__socio == None:
            return self.__limite
        else:
            return self.__limite + self.__socio.__limite
    def set_limite(self, limite):
        self.__limite = limite
    def get_socio(self):
        return self.__socio
    def set_socio(self, socio):   # a.set_socio(b)  self -> a   socio -> b
        self.__socio = socio
        socio.__socio = self
    def __str__(self):
        if self.__socio == None:
            return f"{self.__nome} {self.__limite} {self.get_limite_sociedade()}"
        else:
            return f"{self.__nome} {self.__limite} {self.__socio.__nome} {self.get_limite_sociedade()}"
            

a = Cliente("Alex", 1000)
b = Cliente("Marília", 1500)
c = Cliente("Eduardo", 2000)
d = Cliente("Silvia", 2500)
a.set_socio(b)
d.set_socio(c)