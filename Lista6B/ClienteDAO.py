import Cliente
import json

class ClienteDAO:
    clientes_cadastrados = []

    @classmethod
    def inserir(cls, cliente):
        cls.abrir_json()
        cls.clientes_cadastrados.append(cliente.id)
        cls.salvar_json()
    @classmethod
    def listar(cls):
        cls.abrir_json()
        return cls.clientes_cadastrados
    @classmethod
    def listar_id(cls, id):
        cls.abrir_json()
        for i in cls.clientes_cadastrados:
            if i.get_id() == id:
                return i
        return None
    @classmethod
    def atualizar(cls, cliente):
        cls.abrir_json()
        aux = cls.listar_id(cliente.id)
        if aux != None:
            cls.clientes_cadastrados.remove(cliente.get_id())
            cls.clientes_cadastrados.append(cliente)
        cls.salvar_json()
    @classmethod
    def excluir(cls, cliente):
        cls.abrir_json()
        aux = cls.listar_id(cliente.id)
        if aux != None:
            cls.clientes_cadastrados.remove(cliente.get_id())
        cls.salvar_json()
    @classmethod
    def abrir_json(cls):
        cls.clientes_cadastrados = []
        try: 
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Cliente(dic["id"], dic["nome"], dic["email"], dic["telefone"])
                    cls.clientes_cadastrados.append(c)
        except:
            pass
    @classmethod
    def salvar_json(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.clientes_cadastrados, arquivo, default=vars, indent=4)