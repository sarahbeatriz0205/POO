import json
class Cliente:
    def __init__(self, idCliente, nome, email, telefone):
        self.idCliente = idCliente
        self.nome = nome
        self.email =  email
        self.telefone = telefone
    
    def __str__(self):
        return f"{self.idCliente} - {self.nome} - {self.email} - {self.telefone}"
    
    def to_json(self):
        return {"idCliente" : self.idCliente, "nome" : self.nome, "email" : self.email, "telefone" : self.telefone} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Cliente(dic["idCliente"], dic["nome"], dic["email"], dic["telefone"]) 

class ClienteDAO:
    clientes = []   # atributo da classe ClienteDAO -> DAO = Um objeto usado para acessar e salvar dados de outra classe          
    @classmethod              
    def inserir(cls, obj):
        cls.abrir()
        idC = 0 # aux.idCliente sempre vai ser maior que idC
        for aux in cls.clientes: # aux -> é um objeto da classe Cliente que está armazenado no clientes.json
            if aux.idCliente > idC: idC = aux.idCliente # aux.idCliente -> identifica o id do objeto aux
        obj.idCliente = idC + 1    #obj vai ser o objeto que foi recebido no momento
        cls.clientes.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.clientes
    @classmethod
    def listar_id(cls, idCliente):
        cls.abrir_json() # tenho que abrir o json
        for obj in cls.clientes: # percorrer a lista
            if obj.idCliente == idCliente: return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        # procurar o objeto que tem o idCliente dado por obj.idCliente
        aux = cls.listar_id(obj.idCliente)
        if aux != None: # aux = cliente antigo
            #aux.nome = obj.nome
            cls.clientes.remove(aux)
            cls.clientes.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        # procurar o objeto que tem o idCliente dado por obj.idCliente
        aux = cls.listar_id(obj.idCliente)
        if aux != None:
            cls.clientes.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.clientes, arquivo, default = Cliente.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.clientes = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Cliente.from_json(dic)
                    cls.clientes.append(c)
        except:
            pass            