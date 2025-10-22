class Cliente:
    def __init__(self, id, nome, email, telefone):
        self.__id = id
        self.__nome = nome
        self.__email =  email
        self.__telefone = telefone

    def set_id(self, id):
        if id == None:
            return f"Erro!"
        elif str(id):
            raise TypeError()
        else:
            self.__id = id
    def set_nome(self, nome):
        if nome == "":
            return f"Erro!"
        elif int(nome) or float(nome):
            raise TypeError()
        else:
            self.__nome = nome
    def set_email(self, email):
        if "@" not in email or "gmail.com" not in email:
            return f"Erro!"
        else:
            self.__email = email
    def set_telefone(self, telefone):
        ddd = [11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 93, 94, 95, 96, 97, 98, 99]
        if telefone[:2] not in ddd:
            return f"Erro!"
        else:
            self.__telefone = telefone

    def get_id(self):
        return self._id
    def get_nome(self):
        return self._nome
    def get_email(self):
        return self._email
    def get_telefone(self):
        return self._telefone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__telefone}"



class Venda:
    def __init__(self, id, data, idCliente):
        self.id = id
        self.data = data
        self.carrinho = True
        self.total = 0
        self.idCliente = idCliente