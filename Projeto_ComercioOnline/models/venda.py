from datetime import datetime
import json

class Venda:
    def __init__(self, idCompra, idCliente, total, data = datetime.now()):
        self.set_idCompra(idCompra)
        self.set_data(data) # data e horas atuais; chamar quando a compra for finalizada, ou seja, quando total for 0
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
        return f"ID da compra = {self.__idCompra} - Data = {self.__data} - Total da compra = {self.__total} - ID do cliente = {self.__idCliente}"
        
    def to_json(self):
        return {"idCompra" : self.__idCompra, "data" : self.__data.isoformat(), "idCliente" : self.__idCliente, "Total" : self.__total} # me permite que eu ponha o nome que eu quiser para as chaves
    
    @staticmethod
    def from_json(dic):
        return Venda(dic["idCompra"], dic["idCliente"], dic["Total"], dic["data"])

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
        obj.set_idCompra(obj.get_idCompra() + 1)
        cls.vendas.append(obj)
        cls.salvar_json()
        return obj.get_idCompra()
    @classmethod
    def listar(cls):
        cls.abrir_json() # não pode ser "return cls.abrir_json" porque esse método não retorna nada
        return cls.vendas
    @classmethod
    def listar_meus(cls, idCliente):
        cls.abrir_json() # não pode ser "return cls.abrir_json" porque esse método não retorna nada
        vendas = []
        for objetoVenda in cls.vendas:
            if objetoVenda.get_idCliente() == idCliente: vendas.append(objetoVenda)
        return vendas
    @classmethod
    def listar_idCliente(cls, idCompra, idCliente):
        for obj in cls.vendas:
            if obj.get_idCompra() == idCompra and obj.get_idCliente() == idCliente:
                return obj
        return None
    @classmethod
    def listar_id(cls, idCompra):
        for obj in cls.vendas:
            if obj.get_idCompra() == idCompra:
                return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_idCliente(obj.get_idCompra(), obj.get_idCliente())
        if aux != None:
            cls.vendas.remove(aux)
            cls.vendas.append(obj)
        cls.salvar_json()
    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_idCompra())
        if aux != None:
            cls.vendas.remove(aux)
        cls.salvar_json()
    @classmethod
    def excluir_lote_idCliente(cls, idCliente):
        cls.abrir_json()
        for objeto in cls.vendas:
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