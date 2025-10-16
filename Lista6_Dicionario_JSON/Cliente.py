import json

class Cliente:
    def __init__(self, id, nome, email, telefone):
        self._id = id 
        self._nome = nome 
        self._email = email
        self._telefone = telefone 

    def set_id(self, id):
        self._id = id
    def set_nome(self, nome):
        self._nome = nome
    def set_email(self, email):
        self._email = email
    def set_telefone(self, telefone):
        self._telefone = telefone

    def get_id(self):
        return self._id
    def get_nome(self):
        return self._nome
    def get_email(self):
        return self._email
    def get_telefone(self):
        return self._telefone

    def __str__(self):
        return f"{self._id} - {self._nome} - {self._email} - {self._telefone}"

class ClienteDAO:
    clientes = {} # lista de objetos

    @classmethod
    def inserir(cls, cliente):
        cls.clientes.append(cliente)
    @classmethod
    def listar(cls):
        return cls.clientes
    @classmethod
    def listar_id(cls, id):
        for c in cls.clientes:
            if cls.clientes[c].id == id:
                return cls.clientes[c]
            else:
                return f"Erro! Esse objeto não existe..."
    @classmethod
    def atualizar(cls, novo_cliente):
        pass
    @classmethod
    def excluir(cls, cliente):
        for i in cls.clientes:
            if cls.clientes[i].id == id:
                cls.clientes.remove(cls.clientes[i])
            else:
                return None
    @classmethod
    def abrir_json(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.clientes, arquivo, default=vars)
    @classmethod
    def salvar_json(cls):
        pass