import json
class Produto:
    def __init__(self, idProduto, descricao, preco, estoque, idCategoria):
        self.set_idProduto(idProduto)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_idCategoria(idCategoria)
    
    def set_idProduto(self, idProduto):
        self.__idProduto = idProduto

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_preco(self, preco):
        self.__preco = preco

    def set_estoque(self, estoque):
        self.__estoque = estoque

    def set_idCategoria(self, idCategoria):
        self.__idCategoria = idCategoria

    def get_idProduto(self):
        return self.__idProduto
    def get_descricao(self):
        return self.__descricao
    def get_preco(self):
        return self.__descricao
    def get_descricao(self):
        return self.__descricao
    def get_descricao(self):
        return self.__descricao
    
    def to_json(self):
        return {"id" : self.__idProduto, "descricao" : self.__descricao, "preco" : self.__preco, "estoque" : self.__estoque, "idCategoria" : self.__idCategoria} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["idCategoria"])
    
    def __str__(self):
        return f"ID do produto = {self.__idProduto} - Descrição = {self.__descricao} - Preço = {self.__preco} - Estoque = {self.__estoque} - ID da categoria = {self.__idCategoria}"


class ProdutoDAO:
    produtos = []

    @classmethod
    def inserir(cls, objetoProduto):
        cls.abrir_json()
        idProduto = 0
        for objetoProduto in cls.produtos:
            if objetoProduto.get_idProduto() > idProduto: 
                idProduto = objetoProduto.get_idProduto()
        objetoProduto.set_idProduto(objetoProduto.get_idProduto() + 1)
        cls.produtos.append(objetoProduto)
        cls.salvar_json()
    @classmethod
    def listar(cls):
        cls.abrir_json() # não pode ser "return cls.abrir_json" porque esse método não retorna nada
        return cls.produtos
    @classmethod
    def listar_id(cls, idProduto):
        for obj in cls.produtos:
            if obj.get_idProduto() == idProduto:
                return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_idProduto())
        if aux != None:
            cls.produtos.remove(aux)
            cls.produtos.append(obj)
        cls.salvar_json()
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_idProduto())
        if aux != None:
            cls.produtos.remove(aux)
        cls.salvar_json()
    @classmethod
    def salvar_json(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.produtos, arquivo, default = Produto.to_json, indent=4)
    @classmethod
    def abrir_json(cls):
        cls.produtos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Produto.from_json(dic)
                    cls.produtos.append(c)
        except:
            pass