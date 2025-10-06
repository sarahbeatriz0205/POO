class Cliente:
    def __init__(self, nome, limite):
        self.set_nome(nome)
        self.set_limite(limite)
        self._socio = None
    def set_nome(self, nome):
        self.__nome = nome
    def set_limite(self, limite):
        self.__limite = limite
    def set_socio(self, socio):
        self.__socio = socio
    def get_nome(self):
        return self.__nome
    def get_limite(self):
        return self.__limite
    def get_socio(self):
        return self.__socio