from datetime import datetime
from produto import Produto
import json

class Venda:
    def __init__(self, idCompra, idCliente):
        self.__id = idCompra
        self.data = datetime.now() # data e horas atuais; chamar quando a compra for finalizada, ou seja, quando total for 0
        self.__carrinho = True # false quando total for 0
        self.__total = 0.0 # preciso do id do produto pra pegar o preço
        self.__idCliente = idCliente
    
    def adicionar_item(self):
        if self.__carrinho:
            self.__total += Produto.get_preco()
    
    def finalizar_compra(self):
        if self.__carrinho:
            self.__total = 0.0
            self.__carrinho = False
       

    def set_id(self, idCompra):
        self.__id = idCompra
    
    def set_carrinho(self):
        if self.__total == 0:
            self.__carrinho = False
        else:
            self.__carrinho = True
    
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    
    def set_total(self, total):
        self._total = total

    def get_id(self):
        return self.__id
    def get_carrinho(self):
        return self.__carrinho
    def get_idCliente(self):
        return self.__idCliente
    def get_total(self):
        return self.__total
    
    def __str__(self):
        if self.__carrinho == False: self.__carrinho = str("Compra Finalizada!") 
        return f"{self.__id} - {self.__carrinho} - {self.__idCliente} - {self.__total} - {self.data}"

class VendaDAO:
    venda = []

    @classmethod
    def inserir(cls, venda):
        cls.abrir_json()
        cls.venda.append(venda.id)
        cls.salvar_json()
    @classmethod
    def listar(cls):
        cls.abrir_json()
        return cls.venda
    @classmethod
    def listar_id(cls, id):
        cls.abrir_json()
        for i in cls.venda:
            if i.get_id() == id:
                return i
        return None
    @classmethod
    def atualizar(cls, venda):
        cls.abrir_json()
        aux = cls.listar_id(venda.id)
        if aux != None:
            cls.venda.remove(venda.get_id())
            cls.venda.append(venda)
        cls.salvar_json()
    @classmethod
    def excluir(cls, venda):
        cls.abrir_json()
        aux = cls.listar_id(venda.id)
        if aux != None:
            cls.venda.remove(venda.get_id())
        cls.salvar_json()
        
    @classmethod
    def abrir_json(cls):
        cls.venda = []
        try: 
            with open("venda.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Venda(dic["id"], dic["idCompra"], dic["total"], dic["telefone"])
                    cls.venda.append(c)
        except:
            pass
    @classmethod
    def salvar_json(cls):
        with open("venda.json", mode="w") as arquivo:
            json.dump(cls.venda, arquivo, default=vars, indent=4)