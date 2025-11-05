from models.Cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.produto import Produto, ProdutoDAO 

class View:
    def cliente_criar_admin(nome, email, telefone, senha):
        id = 0
        for obj in ClienteDAO.listar():
            if obj.email == "@admin.com": return
        ClienteDAO.inserir(Cliente(id, nome, email, telefone, senha)) # se o if não for verdadeiro, ele passa para a próxima linha e cria um novo admin
    def cliente_inserir(nome, email, telefone, senha):
        id = 0
        ClienteDAO.inserir(Cliente(id, nome, email, telefone, senha))
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    def cliente_atualizar(id, nome, email, telefone, senha):
        c = Cliente(id, nome, email, telefone, senha)
        ClienteDAO.atualizar(c)
    def cliente_excluir(id, nome, email, telefone):
        c = Cliente(id, nome, email, telefone)
        ClienteDAO.excluir(c)

    def categoria_inserir(descricao):
        id = 0
        CategoriaDAO.inserir(Categoria(id, descricao))
    def categoria_listar():
        return CategoriaDAO.listar()
    def categoria_listar_id(id):
        return CategoriaDAO.listar_id(id)
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
<<<<<<< HEAD
    def produto_listar_id(id):
        return ProdutoDAO.listar_id(id)
    def produto_atualizar(id, descricao, preco, estoque):
        c = Produto(id, descricao, preco, estoque)
        ProdutoDAO.atualizar(c)
    def produto_excluir(id):
        c = Produto(id)
        ProdutoDAO.excluir(c)
    def produto_reajuste(percentual):
        for obj in ProdutoDAO.listar():
            obj.preco = obj.preco * (1 + percentual)
            ProdutoDAO.atualizar(obj)
=======
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        c = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.atualizar(c)
    def produto_excluir(id, descricao, preco, estoque, idCategoria):
        c = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.excluir(c)
>>>>>>> refs/remotes/origin/main
