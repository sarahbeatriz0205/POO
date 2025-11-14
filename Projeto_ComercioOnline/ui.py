from views import View

class UI:  
    __usuario = None

    def menu_visitante():
        print("1-Entrar no Sistema, 2-Abrir Conta, 9-Fim")
        op = int(input("Informe uma opção: "))           
        if op == 1: UI.visitante_entrar()
        if op == 2: UI.visitante_criar_conta()
        return op  

    def menu_admin():
        print("\n")
        print("Seja Bem Vindo(a), Administrador(a)!")
        print("\n")
        print("Clientes")
        print("1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir")
        print()
        print("Categorias")
        print("5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir")
        print()
        print("Produtos")
        print("9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir")
        print()
        print("13 - Fim")
        op = 0
        while op != 13:
            op = int(input("Informe uma opção: "))
        
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()
            if op == 9: UI.produto_inserir()
            if op == 10: UI.produto_listar()
            if op == 11: UI.produto_atualizar()
            if op == 12: UI.produto_excluir()
            if op == 13: UI.usuario_sair()
      
    def menu_cliente():
        print("\n")
        print("1-Listar produtos")
        print("2-Inserir produto no carrinho")
        print("3-Visualizar carrinho")
        print("4-Comprar carrinho")
        print("5-Listar minhas compras")
        print("9-Sair")
        op = 0
        while op != 9:
            op = int(input("Informe uma opção: "))  
                 
            if op == 1: UI.listar_produtos()
            if op == 2: UI.inserir_produto()
            if op == 3: UI.estado_carrinho()
            if op == 4: UI.finalizar_compra()
            if op == 5: UI.listar_compras()
            if op == 9: UI.usuario_sair() 
        return op       
    def main():
        View.cliente_criar_admin("admin", "admin")
        UI.menu_visitante()
        
    @classmethod
    def visitante_entrar(cls):
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        cls.__usuario = View.cliente_autenticar(email, senha)
        if cls.__usuario == None: print("Usuário ou senha inválidos")
        if email == "admin": UI.menu_admin()
        else: 
            for obj in View.cliente_listar():
                if email == obj.get_email(): UI.menu_cliente()

    def visitante_criar_conta():
        UI.cliente_inserir()
    
    @classmethod
    def usuario_sair(cls):
        cls.__usuario = None

    def cliente_inserir():
        # id = 0
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        telefone = int(input("Informe seu número de telefone: "))
        senha = input("Informe sua senha: ")
        View.cliente_inserir(nome, email, telefone, senha)
    def cliente_listar():
        for obj in View.cliente_listar(): 
            print(obj)     
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        telefone = int(input("Informe o novo número"))
        senha = input("Nova senha: ")
        View.cliente_atualizar(id, nome, email, telefone, senha)
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id a ser excluído: "))
        nome = ""
        email = ""
        telefone = 0
        senha = ""
        View.cliente_excluir(id, nome, email, telefone, senha)

    def categoria_inserir():
        # id = 0
        descricao = input("Informe a descrição: ")
        View.categoria_inserir(descricao)
    def categoria_listar():
        for obj in View.categoria_listar():
            print(obj)       
    def categoria_atualizar():
        UI.categoria_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        View.categoria_atualizar(id, descricao)
    def categoria_excluir():
        UI.categoria_listar()
        id = int(input("Informe o id a ser excluído: "))
        descricao = ""
        View.categoria_excluir(id, descricao)
    
    def produto_inserir():
        id = 0
        descricao = input("Informe a descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Quanto tem no estoque: "))
        idCategoria = int(input("Id da categoria: "))
        View.produto_inserir(id, descricao, preco, estoque, idCategoria)
    def produto_listar():
        for obj in View.produto_listar():
            print(obj)       
    def produto_atualizar():
        UI.produto_listar()
        id = int(input("Informe o id a ser atualizado: "))
        descricao = input("Informe a nova descrição: ")
        preco = float(input("Informe o novo preço: "))
        estoque = int(input("Informe a nova quantidade do estoque: "))
        idCategoria = int(input("Qual a categoria: "))
        View.produto_atualizar(id, descricao, preco, estoque, idCategoria)
    def produto_excluir():
        UI.produto_listar()
        id = int(input("Informe o id a ser excluído: "))
        descricao = ""
        preco = 0.0
        estoque = 0
        idCategoria = 0
        View.produto_excluir(id, descricao, preco, estoque, idCategoria)
    def produto_reajuste():
        UI.produto_listar()
        percentual = float(input("Informe o percentual de ajuste: "))
        View.produto_reajuste(percentual)

    def listar_produtos():
        descricao = input("Qual produto você deseja buscar? ")
        resultado = View.listar_produtos(descricao)
        print(resultado)
    def inserir_produto():
        View.inserir_produto()


UI.main()