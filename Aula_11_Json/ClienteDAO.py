class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.nome} - {self.id}"

# C.R.U.D  
class ClienteDAO:
    clientes = []
    @classmethod
    def inserir(cls, cliente):
        if any(c.id == cliente.id for c in self.clientes):
            print(f"Erro: já existe um cliente com o ID {cliente.id}")
        else:
            cls.clientes.append(cliente)
    @classmethod
    def listar(cls):
        return cls.clientes
    @classmethod
    def atualizar(cls, novo_nome):
        for cliente in cls.clientes:
            if cliente.id == novo_nome.id:
                cliente.nome = novo_nome.nome
    @classmethod
    def excluir(cls, cliente):
        for obj in cls.clientes:
            if obj.id == cliente.id:
                cls.clientes.remove(obj)