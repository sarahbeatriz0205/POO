import json
class Cliente:
    def __init__(self, id, nome, email, telefone):
        self.__id = id
        self.__nome = nome
        self.__email =  email
        self.__telefone = telefone
    
    def to_json(self):
        return {"id" : self.__id, "nome" : self.__nome, "email" : self.__email, "telefone" : self.__telefone} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["telefone"]) 

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
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_telefone(self):
        return self.__telefone

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__telefone}"



class ClienteDAO:             # classe estática -> não tem instância
    objetos = []              # atributo da classe
    @classmethod              # classe DAO não vai ter instância
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.id > id: id = aux.id
        obj.id = id + 1    
        cls.objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id: return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.id)
        if aux != None:
            #aux.nome = obj.nome
            # remove o objeto antigo aux e insere o novo obj
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.id)
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("clientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Cliente(dic["id"], dic["nome"])
                    cls.objetos.append(c)
        except:
            pass            