class Categoria:
    def __init__(self, descricao):
        self.__descricao = descricao

class Produto:
    def __init__(self, descricao, preco, estoque):
        self.__descricao = descricao
        self.__preco = preco
        self.__estoque = estoque

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