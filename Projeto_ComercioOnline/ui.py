from views import View

class UI:  
    __usuario = None

    def menu_visitante():
        print("1-Entrar no Sistema, 2-Abrir Conta, 9-Fim")
        op = int(input("Informe uma opção: "))           
        if op == 1: UI.visitante_entrar()
        if op == 2: UI.visitante_criar_conta()
        return op  

    # tá tudo ok por enquanto
    def menu_admin():
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
        return int(input("Informe uma opção: ")) 
      
    def menu_cliente():
        print("1-Listar produtos")
        print("2-Inserir produto no carrinho")
        print("3-Visualizar carrinho")
        print("4-Comprar carrinho")
        print("5-Listar minhas compras")
        print("9-Sair")
        op = int(input("Informe uma opção: "))           
        if op == 1: UI.listar_produtos()
        if op == 2: pass
        if op == 3: pass
        if op == 4: pass
        if op == 5: pass
        if op == 9: UI.usuario_sair()        
    def main():
        UI.menu_visitante()
        View.cliente_criar_admin(UI.visitante_entrar()) #TypeError: View.cliente_criar_admin() missing 1 required positional argument: 'senha' -> ajeitar no Views
    
    @classmethod
    def menu(cls):
        op = 0
        while op != 9:
            if cls.__usuario == None: 
                # usuário não está logado
                op = UI.menu_visitante()
            else:
                # usuário está logado, verifica se é o admin
                admin = cls.__usuario["nome"] == "admin"
                # mensagem de bem-vindo
                print("IF Comércio Eletrônico 2025")
                print("Bem-vindo(a), " + cls.__usuario["nome"])
                # menu do usuário: admin ou cliente
                if admin: UI.menu_admin()
                else: UI.menu_cliente()
    @classmethod
    def visitante_entrar(cls):
        email = input("Informe o e-mail: ")
        senha = input("Informe a senha: ")
        cls.__usuario = View.cliente_autenticar(email, senha)
        if cls.__usuario == None: print("Usuário ou senha inválidos")

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
        # NÃO É NECESSÁRIO CRIAR O OBJETO QUANDO EXISTE O VIEW
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
        descricao = input("Informe a descrição: ")
        preco = float(input("Preço: "))
        estoque = int(input("Quanto tem no estoque: "))
        idCategoria = int(input("Id da categoria: "))
        View.produto_inserir(descricao, preco, estoque, idCategoria)
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
        UI.produto_listar()
        nome = input("Qual produto você deseja buscar? ")
        View.listar_produtos(nome)


UI.main()