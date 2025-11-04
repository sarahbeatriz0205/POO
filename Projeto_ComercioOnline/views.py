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
    def cliente_excluir(id, nome, email, telefone):
        c = Cliente(id, nome, email, telefone)
        ClienteDAO.excluir(c)

    def categoria_inserir(descricao):
        id = 0
        CategoriaDAO.inserir(Categoria(id, descricao))
    def categoria_listar():
        return CategoriaDAO.listar()
    def categoria_atualizar(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO.atualizar(c)
    def categoria_excluir(id, descricao):
        c = Categoria(id, descricao)
        CategoriaDAO.excluir(c)

    def produto_inserir(descricao, preco, estoque, idCategoria):
        id = 0
        ProdutoDAO.inserir(Produto(id, descricao, preco, estoque, idCategoria))
    def produto_listar():
        return ProdutoDAO.listar()
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        c = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.atualizar(c)
    def produto_excluir(id, descricao, preco, estoque, idCategoria):
        c = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.excluir(c)