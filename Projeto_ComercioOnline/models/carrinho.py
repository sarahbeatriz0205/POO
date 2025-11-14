import json

class Carrinho:
    def __init__(self, idProduto, qtd):
        self.set_idProduto(idProduto)
        self.set_qtd(qtd)
    
    def get_idProduto(self):
        return self.__idProduto
    def get_qtd(self):
        return self.__qtd
    
    def __str__(self):
        return f"{self.__id} - {self.__qtd}"
    
    def to_json(self):
        return {"id" : self.__idProduto, "descricao" : self.__qtd}
    def from_json(dic):
        return Carrinho(dic["id"], dic["quantidade"]) 

class CarrinhoDAO:
    objetos = []             
    @classmethod              
    def inserir(cls, obj):
        aux = CarrinhoDAO.listar_id(obj.get_idProduto())
        if aux == None:
            cls.objetos.append(obj)
            cls.salvar()
        else:
            aux.qtd += obj.qtd
            cls.atualizar(aux)
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_idProduto() == id: return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_idProduto())
        if aux != None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_idProduto())
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("carrinho.json", mode="w") as arquivo:
                json.dump(cls.objetos, arquivo, default = Carrinho.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("carrinho.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Carrinho.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            