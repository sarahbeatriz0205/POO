from datetime import datetime
import json

class Venda:
    def __init__(self, idCompra, idCliente):
        self.idCompra = idCompra
        self.data = datetime.now() # data e horas atuais; chamar quando a compra for finalizada, ou seja, quando total for 0
        self.total = 0.0 # preciso do id do produto pra pegar o preço
        self.idCliente = idCliente
    
    def __str__(self):
        return f"ID da compra = {self.idCompra} - Data = {self.data} - Estado do carrinho = {self.carrinho} - Total da compra = {self.total} - ID do cliente = {self.idCliente}"
        
    def to_json(self):
        return {"idCompra" : self.idCompra, "data" : self.data.isoformat(), "idCliente" : self.idCliente, "Total" : self.total} # me permite que eu ponha o nome que eu quiser para as chaves
    
    @staticmethod
    def from_json(dic):
        return Venda(dic["idCompra"], dic["data"], dic["idCliente"], dic["Total"])

    
   

class VendaDAO:
    # atributo de VendaDAO:
    vendas = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir_json()
        idCompra = 0
        for objetoVenda in cls.vendas:
            if objetoVenda.idCompra > idCompra: 
                idCompra = objetoVenda.idCompra
        obj.idCompra = obj.idCompra + 1
        cls.vendas.append(obj)
        cls.salvar_json()
        return obj.idCompra
    @classmethod
    def listar(cls):
        cls.abrir_json() # não pode ser "return cls.abrir_json" porque esse método não retorna nada
        return cls.vendas
    @classmethod
    def listar_id(cls, idCompra):
        for obj in cls.vendas:
            if obj.idCompra == idCompra:
                return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.idCompra)
        if aux != None:
            cls.vendas.remove(aux)
            cls.vendas.append(obj)
        cls.salvar_json()
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.idCompra)
        if aux != None:
            cls.vendas.remove(aux)
        cls.salvar_json()
    @classmethod
    def salvar_json(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump(cls.vendas, arquivo, default = Venda.to_json, indent=4)
    @classmethod
    def abrir_json(cls):
        cls.vendas = []
        try:
            with open("vendas.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Venda.from_json(dic)
                    cls.vendas.append(c)
        except:
            pass