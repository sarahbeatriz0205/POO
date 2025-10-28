import json
class Produto:
    def __init__(self, idProduto, descricao, preco, estoque, idCategoria):
        self.idProduto = idProduto
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria
    
    def to_json(self):
        return {"id" : self.__idProduto, "descricao" : self.__descricao, "preco" : self.__preco, "estoque" : self.__estoque, "idCategoria" : self.idCategoria} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["idCategoria"])
    
    def __str__(self):
        return f"ID do produto = {self.idProduto} - Descrição = {self.descricao} - Preço = {self.preco} - Estoque = {self.estoque} - ID da categoria = {self.idCategoria}"


class ProdutoDAO:
    produtos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir_json()
        idCompra = 0
        for objetoProduto in cls.produtos:
            if objetoProduto.idProduto > idProduto: 
                idProduto = objetoProduto.idProduto
        objetoProduto.idProduto = objetoProduto.idProduto + 1
        cls.vendas.append(obj)
        cls.salvar_json()
    @classmethod
    def listar(cls):
        cls.abrir_json() # não pode ser "return cls.abrir_json" porque esse método não retorna nada
        return cls.produtos
    @classmethod
    def listar_id(cls, idProduto):
        for obj in cls.vendas:
            if obj.idProduto == idProduto:
                return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.idProduto)
        if aux != None:
            cls.vendas.remove(aux)
            cls.vendas.append(obj)
        cls.salvar_json()
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.idProduto)
        if aux != None:
            cls.vendas.remove(aux)
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