import json
class Produto:
    def __init__(self, idProduto, descricao, preco, estoque, idCategoria):
        self.__idProduto = idProduto
        self.__descricao = descricao
        self.__preco = preco # float
        self.__estoque = estoque # int
        self.idCategoria = idCategoria
    
    @staticmethod
    def to_json(self):
        return {"id" : self.__idProduto, "descricao" : self.__descricao, "preco" : self.__preco, "estoque" : self.__estoque, "idCategoria" : self.idCategoria} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["idCategoria"]) 


    def set_idProduto(self, idProduto):
        self.__idProduto = idProduto
    
    def set_descricao(self, nova_descricao):
        self.__descricao = nova_descricao
    
    def set_preco(self, preco):
        self.__preco = preco

    def set_estoque(self, estoque):
        self.__estoque = estoque
    
    def get_idProduto(self):
        return self.__idProduto

    def get_descricao(self):
        return self.__descricao
    
    def get_preco(self):
        return self.__preco
    
    def get_estoque(self):
        return self.__estoque
    

class ProdutoDAO:
    produtos_cadastrados = []

    @classmethod
    def inserir(cls, produtos):
        cls.abrir_json()
        cls.produtos_cadastrados.append(produtos.id)
        cls.salvar_json()
    @classmethod
    def listar(cls):
        cls.abrir_json()
        return cls.produtos_cadastrados
    @classmethod
    def listar_id(cls, id):
        cls.abrir_json()
        for i in cls.produtos_cadastrados:
            if i.get_id() == id:
                return i
        return None
    @classmethod
    def atualizar(cls, produtos):
        cls.abrir_json()
        aux = cls.listar_id(produtos.id)
        if aux != None:
            cls.produtos_cadastrados.remove(produtos.get_id())
            cls.produtos_cadastrados.append(produtos)
        cls.salvar_json()
    @classmethod
    def excluir(cls, produtos):
        cls.abrir_json()
        aux = cls.listar_id(produtos.id)
        if aux != None:
            cls.produtos_cadastrados.remove(produtos.get_id())
        cls.salvar_json()
    @classmethod
    def abrir_json(cls):
        cls.produtos_cadastrados = []
        try: 
            with open("produtos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Produto.from_json()
                    cls.produtos_cadastrados.append(c)
        except:
            pass
    @classmethod
    def salvar_json(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.produtos_cadastrados, arquivo, default = Produto.to_json(), indent=4)
    