# classe view vai importar as classes Entidade e as DAO

from models.Cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.produto import Produto, ProdutoDAO 

class View:
    def cliente_inserir(nome, email, telefone):
        id = 0
        ClienteDAO.inserir(Cliente(id, nome, email, telefone))
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_atualizar(id, nome, email, telefone):
        c = Cliente(id, nome, email, telefone)
        ClienteDAO.atualizar(c)
    def cliente_excluir(id):
        pass

    def categoria_inserir(descricao):
        id = 0
        CategoriaDAO.inserir(Categoria(id, descricao))
    def categoria_listar():
        return CategoriaDAO.listar()
    def categoria_atualizar(id, descricao):
        c = Cliente(id, descricao)
        CategoriaDAO.atualizar(c)
    def categoria_excluir(id):
        pass

    def produto_inserir(descricao, preco, estoque):
        id = 0
        ProdutoDAO.inserir(Produto(id, descricao, preco, estoque))
    def produto_listar():
        return ProdutoDAO.listar()
    def produto_atualizar(id, descricao, preco, estoque):
        c = Cliente(id, descricao, preco, estoque)
        ProdutoDAO.atualizar(c)
    def produto_excluir(id):
        pass

    # FAZER O VIEW DO PRODUTO