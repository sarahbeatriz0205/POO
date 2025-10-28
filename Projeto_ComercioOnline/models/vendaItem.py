import json
class VendaItem:
    def __init__(self, idVendaItem, quantidade, preco, idVenda, idProduto):
        self.idVendaItem = idVendaItem
        self.quantidade = quantidade
        self.preco = preco
        self.idVenda = idVenda
        self.idProduto = idProduto
    
    def to_json(self):
        return {"idVendaItem" : self.idVendaItem, "quantidade" : self.quantidade, "preco" : self.preco, "idVenda" : self.idVenda, "idProduto" : self.idProduto} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return VendaItem(dic["idVendaItem"], dic["quantidade"], dic["preco"], dic["idVenda"], dic["idVenda"], dic["idProduto"]) 
    def __str__(self):
        return f""
    
class VendaItemDAO:
    venda_item = []

    @classmethod
    def inserir(cls, objeto):
        cls.abrir_json()
        idVendaItem = 0 # aux.idCliente sempre vai ser maior que idC
        for aux in cls.venda_item: # aux -> é um objeto da classe Cliente que está armazenado no clientes.json
            if aux.idVendaItem > idVendaItem: idVendaItem = aux.idVendaItem # aux.idCliente -> identifica o id do objeto aux
        objeto.idVendaItem = idVendaItem + 1    #obj vai ser o objeto que foi recebido no momento
        cls.venda_item.append(objeto)
        cls.salvar_json()
    @classmethod
    def listar(cls):
        cls.abrir_json()
        return cls.venda_item
    @classmethod
    def listar_id(cls, idVendaItem):
        cls.abrir_json()
        for objetoVendaItem in cls.venda_item:
            if objetoVendaItem.idVendaItem == idVendaItem:
                return objetoVendaItem
            return None
    @classmethod
    def atualizar(cls, objetoVendaItem):
        aux = cls.listar_id(objetoVendaItem.idVendaItem)
        if aux != None:
            cls.venda_item.remove(aux)
            cls.venda_item.append(objetoVendaItem)
    @classmethod
    def excluir(cls, objetoVendaItem):
        aux = cls.listar_id(objetoVendaItem.idVendaItem)
        if aux != None:
            cls.venda_item.remove(aux)
            cls.salvar_json()
    @classmethod
    def salvar_json(cls):
        with open("venda_itens.json", mode="w") as arquivo:
            json.dump(cls.venda_item, arquivo, default = VendaItem.to_json, indent = 4)
    @classmethod
    def abrir_json(cls):
        cls.venda_item = []
        try:
            with open("venda_itens.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = VendaItem.from_json(dic)
                    cls.clientes.append(c)
        except:
            pass