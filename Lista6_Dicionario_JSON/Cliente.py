import json

class Cliente:
    def __init__(self, id, nome, email, telefone):
        self._id = id # atributo de instância (id, nome, email, telefone)
        self._nome = nome 
        self._email = email
        self._telefone = telefone 

    def set_id(self, id):
        self._id = id
    def set_nome(self, nome):
        self._nome = nome
    def set_email(self, email):
        self._email = email
        # validar o e-mail
    def set_telefone(self, telefone):
        self._telefone = telefone
        # validar o telefone com o DDD

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

class ClienteDAO: # classe estática - não tem instância
    clientes = [] # lista de objetos; atributo da classe

    @classmethod # classe DAO não vai ter instância
    def inserir(cls, cliente):
        cls.abrir_json()
        id = 0
        for aux in cls.clientes:
            if aux.id > id: 
                id = aux.id
            aux.id += 1
        cls.clientes.append(cliente)
        cls.salvar_json() # chama o método salvar_json para salvar os dados inseridos
    @classmethod
    def listar(cls):
        cls.abrir_json()
        return cls.clientes
    @classmethod
    def listar_id(cls, id):
        cls.abrir_json()
        for c in cls.clientes:
            if c.id == id:
                return c
        return None
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.id) # procurar o objeto que tem o id dado por obj.id
        if aux != None:
            cls.clientes.remove(aux)
            cls.clientes.append(obj.id)
        cls.salvar_json()
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.id)
        if aux != None:
             cls.clientes.remove(obj.id)
        cls.salvar_json()
    @classmethod
    def abrir_json(cls):
        cls.clientes = []
        try: 
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo) # abrindo o json
                for dic in list_dic:
                    c = Cliente(dic["id"], dic["nome"], dic["email"], dic["telefone"])
                    cls.clientes.append(c)
        except: # retorna erro se o arquivo não existir
            pass
    @classmethod
    def salvar_json(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.clientes, arquivo, default=vars, indent=4)

class UI:     
    def menu():
        print("1-Inserir, \n2-Listar, \n3-Atualizar, \n4-Excluir, \n5-Fim")
        return int(input("Informe uma opção: "))           
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: UI.inserir()
            if op == 2: UI.listar()
            if op == 3: UI.atualizar()
            if op == 4: UI.excluir()
    def inserir():
        id = 0
        nome = input("Informe o nome: ")
        email = input("Informe seu e-mail: ")
        telefone = input("Informe seu número de telefone: ")
        c = Cliente(id, nome, email, telefone)
        ClienteDAO().inserir(c)
    def listar():
        c = ClienteDAO.listar()
        print(c)        
    def atualizar():
        UI.listar()
        id = int(input("Informe o id que você quer atualizar: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        telefone = input("Informe o novo telefone: ")

    def excluir():
        UI.listar()
        id = int(input("Informe o id que você quer excluir: "))   
        nome = None 
        email = None 
        telefone = None

UI.main()