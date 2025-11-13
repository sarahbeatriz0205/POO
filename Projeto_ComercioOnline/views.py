from models.cliente import Cliente, ClienteDAO
from models.categoria import Categoria, CategoriaDAO
from models.produto import Produto, ProdutoDAO 
from models.vendaItem import VendaItem, VendaItemDAO
from models.venda import Venda, VendaDAO

class View:
    @staticmethod
    def cliente_criar_admin(email, senha):
        id = 0
        nome = ""
        telefone = 0
        for obj in ClienteDAO.listar():
            if obj.get_email() == "admin": return
        ClienteDAO.inserir(Cliente(id, nome, email, telefone, senha)) # se o if não for verdadeiro, ele passa para a próxima linha e cria um novo admin
    @staticmethod
    def cliente_autenticar(email, senha):
        for obj in View.cliente_listar():
            if obj.get_email() == email: 
                return { "email": obj.get_email(), "senha" : obj.get_senha()}
        return None
    def cliente_inserir(nome, email, telefone, senha):
        id = 0
        c = Cliente(id, nome, email, telefone, senha)
        ClienteDAO.inserir(c)
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_listar_id(id):
        return ClienteDAO.listar_id(id)
    def cliente_atualizar(id, nome, email, telefone, senha):
        c = Cliente(id, nome, email, telefone, senha)
        ClienteDAO.atualizar(c)
    def cliente_excluir(id, nome, email, telefone, senha):
        c = Cliente(id, nome, email, telefone, senha)
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
            obj.set_preco(obj.get_preco() * (1 + percentual))
            ProdutoDAO.atualizar(obj.get_preco)
    def produto_atualizar(id, descricao, preco, estoque, idCategoria):
        c = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.atualizar(c)
    def produto_excluir(id, descricao, preco, estoque, idCategoria):
        c = Produto(id, descricao, preco, estoque, idCategoria)
        ProdutoDAO.excluir(c)
    def listar_produtos(nome):
        for obj in ProdutoDAO.listar():
            if obj.get_nome() == nome:
                if obj.get_estoque() == None:
                    return obj
            return None
    
    def inserir_produto():
        pass
    def estado_carrinho():
        pass
    def finalizar_compra():
        pass
    def listar_compras():
        pass
    def mostrar_comprovante():
        pass
            