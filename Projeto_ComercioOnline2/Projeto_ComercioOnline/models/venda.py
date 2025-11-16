from datetime import datetime
import json

class Venda:
    def __init__(self, idCompra, idCliente, total):
        self.set_idCompra(idCompra)
        self.set_data(datetime.now()) # data e horas atuais; chamar quando a compra for finalizada, ou seja, quando total for 0
        self.set_total(total) # preciso do id do produto pra pegar o preço
        self.set_idCliente(idCliente)
    
    def set_idCompra(self, idCompra):
        self.__idCompra = idCompra
    def set_data(self, data):
        self.__data = data
    def set_total(self, total):
        self.__total = total
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    
    def get_idCompra(self):
        return self.__idCompra
    def get_data(self):
        return self.__data
    def get_total(self):
        return self.__total
    def get_idCliente(self):
        return self.__idCliente
    
    def __str__(self):
        return f"ID da compra = {self.idCompra} - Data = {self.data} - Estado do carrinho = {self.carrinho} - Total da compra = {self.total} - ID do cliente = {self.idCliente}"
        
    def to_json(self):
        return {"idCompra" : self.idCompra, "data" : self.data.isoformat(), "idCliente" : self.idCliente, "Total" : self.total} # me permite que eu ponha o nome que eu quiser para as chaves
    
    @staticmethod
    def from_json(dic):
        return Venda(dic["idCompra"], dic["data"], dic["idCliente"], dic["Total"])

    
   

class VendaDAO:
    # atributo de VendaDAO:
    vendas : list[Venda] = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir_json()
        idCompra = 0
        for objetoVenda in cls.vendas:
            if objetoVenda.get_idCompra() > idCompra: 
                idCompra = objetoVenda.get_idCompra()
        obj.set_idCompra(obj.idCompra + 1)
        cls.vendas.append(obj)
        cls.salvar_json()
        return obj.get_idCompra()
    @classmethod
    def listar(cls):
        cls.abrir_json() # não pode ser "return cls.abrir_json" porque esse método não retorna nada
        return cls.vendas
    def listar_meus(cls, idCliente):
        cls.abrir_json() # não pode ser "return cls.abrir_json" porque esse método não retorna nada
        vendas = []
        for objetoVenda in cls.vendas:
            if objetoVenda.get_idCompra() == idCliente: vendas.append(objetoVenda)
        return vendas
    @classmethod
    def listar_id(cls, idCompra, idCliente):
        for obj in cls.vendas:
            if obj.get_idCompra() == idCompra and obj.get_idCliente() == idCliente:
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
    def excluir_lote_idCliente(cls, idCliente):
        cls.abrir()
        for objeto in cls.objetos:
            if objeto.get_idCliente() == idCliente:
                cls.excluir(objeto)
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