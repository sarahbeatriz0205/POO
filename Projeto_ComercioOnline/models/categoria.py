import json
class Categoria:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao

    def __str__(self):
        return f"{self.id} - {self.descricao}"
    
    def to_json(self):
        return {"id" : self.__id, "descricao" : self.__descricao} # me permite que eu ponha o nome que eu quiser para as chaves
    @staticmethod
    def from_json(dic):
        return Categoria(dic["id"], dic["descricao"]) 
    

class CategoriaDAO:
    objetos = []             
    @classmethod              
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.id > id: id = aux.id
        obj.id = id + 1    
        cls.objetos.append(obj)
        cls.salvar()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id: return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.id)
        if aux != None:
            #aux.nome = obj.nome
            # remove o objeto antigo aux e insere o novo obj
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        # procurar o objeto que tem o id dado por obj.id
        aux = cls.listar_id(obj.id)
        if aux != None:
            cls.objetos.remove(aux)
            cls.salvar()
    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Categoria.to_json, indent=4)
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("categorias.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    c = Categoria.from_json(dic)
                    cls.objetos.append(c)
        except:
            pass            


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