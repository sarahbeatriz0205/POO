class Funcionario: #Superclasse - Classe Base
    def __init__(self, nome, salarioBase):
        self.__nome = nome
        self._salarioBase = salarioBase
    
    def get_nome(self):
        return self.__nome
    def get_salarioBase(self):
        return self._salarioBase
    def __str__(self): # aqui também tem polimorfismo, porque a classe Object (classe base de todas as classes) já tem um método __str__
        return f"{self.__nome} - {self.get_salarioBase()}" # aqui, ele está chamando o get_salarioBase da classe Gerente
    
class Gerente(Funcionario): # Classe descendente
    def __init__(self, nome, salarioBase, gratificacao):
        super().__init__(nome, salarioBase) # super: chama o construtor da classe ancestral
        self.__gratificacao = gratificacao # private

        # self.__nome = nome
        # self.__salarioBase = salarioBase
        # self.__gratificacao = gratificacao
    
    def get_salarioBase(self):
        return self._salarioBase + self.__gratificacao # dessa maneira, tem que ser protected
        # return super().get_salarioBase() + self.__gratificacao ----> essa alternativa permite a utilização do atributo salário mesmo sendo private

# protected: inacessível de fora, mas acessível em uma hierarquia. em Python: self._atributo