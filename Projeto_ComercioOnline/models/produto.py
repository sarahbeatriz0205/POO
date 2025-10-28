import json
class Produto:
    def __init__(self, idProduto, descricao, preco, estoque, idCategoria):
        self.idProduto = idProduto
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.idCategoria = idCategoria
    
    def to_json(self):
        return {"id" : self.idProduto, "descricao" : self.descricao, "preco" : self.preco, "estoque" : self.estoque, "idCategoria" : self.idCategoria} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"], dic["idCategoria"])
    
    def __str__(self):
        return f"ID do produto = {self.idProduto} - Descrição = {self.descricao} - Preço = {self.preco} - Estoque = {self.estoque} - ID da categoria = {self.idCategoria}"


class ProdutoDAO:
    produtos = []

    @classmethod
    def inserir(cls, objetoProduto):
        cls.abrir_json()
        idProduto = 0
        for objetoProduto in cls.produtos:
            if objetoProduto.idProduto > idProduto: 
                idProduto = objetoProduto.idProduto
        objetoProduto.idProduto = objetoProduto.idProduto + 1
        cls.produtos.append(objetoProduto)
        cls.salvar_json()
    @classmethod
    def listar(cls):
        cls.abrir_json() # não pode ser "return cls.abrir_json" porque esse método não retorna nada
        return cls.produtos
    @classmethod
    def listar_id(cls, idProduto):
        for obj in cls.produtos:
            if obj.idProduto == idProduto:
                return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.idProduto)
        if aux != None:
            cls.produtos.remove(aux)
            cls.produtos.append(obj)
        cls.salvar_json()
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.idProduto)
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