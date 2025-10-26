import json
class Categoria:
    def __init__(self, id, descricao):
        self.__id = id
        self.__descricao = descricao

    def set_id(self, id):
        pass
    def set_descricao(self, descricao):
        pass

    def get_id(self):
        return self._id
    def get_descricao(self):
        return self.__descricao

    def __str__(self):
        return f"{self.__id} - {self.__descricao}"
    
    @staticmethod
    def to_json(self):
        return {"id" : self.__id, "descricao" : self.__descricao} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"]) 
    

class CategoriaDAO:
    categoria = []

    @classmethod
    def inserir(cls, categoria):
        cls.abrir_json()
        cls.categoria.append(categoria.id)
        cls.salvar_json()
    @classmethod
    def listar(cls):
        cls.abrir_json()
        return cls.categoria
    @classmethod
    def listar_id(cls, id):
        cls.abrir_json()
        for i in cls.categoria:
            if i.get_id() == id:
                return i
        return None
    @classmethod
    def atualizar(cls, categoria):
        cls.abrir_json()
        aux = cls.listar_id(CategoriaDAO.id)
        if aux != None:
            cls.categoria.remove(categoria.get_id())
            cls.categoria.append(categoria)
        cls.salvar_json()
    @classmethod
    def excluir(cls, categoria):
        cls.abrir_json()
        aux = cls.listar_id(categoria.id)
        if aux != None:
            cls.categoria.remove(categoria.get_id())
        cls.salvar_json()
    @classmethod
    def abrir_json(cls):
        cls.categoria = []
        try: 
            with open("categorias.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Categoria.from_json(dic)
                    cls.categoria.append(c)
        except:
            pass
    @classmethod
    def salvar_json(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.categoria, arquivo, default = Categoria.to_json, indent=4)


# na criação de um objeto, dizer a categoria com base no objeto de categoria
# ligação entre os arquivos json
# a classe que tem asterisco recebe o id da outra e permite que esse id se repita
# preço VendaItem: preço que o cliente guardou no momento da venda
# preço Produto: preço do produto, passível de mudança
# calcular o total, não precisa armazenar
# composição diagrama UML
# * = várias coisas de algo / 1 = uma coisa de algo
# if Venda == None: VendaItem não existe
# carrinho = True enquanto a Venda tiver rolando e ainda não foi paga / carrinho = False quando a Venda for paga