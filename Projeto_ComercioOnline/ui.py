from views import View

class UI:    
    def menu():
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
    def main():
        op = 0
        while op != 14:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
            if op == 5: UI.categoria_inserir()
            if op == 6: UI.categoria_listar()
            if op == 7: UI.categoria_atualizar()
            if op == 8: UI.categoria_excluir()
            if op == 9: UI.produto_inserir()
            if op == 10: UI.produto_listar()
            if op == 11: UI.produto_atualizar()
            if op == 12: UI.produto_excluir()
            if op == 13: UI.produto_reajustar() # criar o produto_reajustar no DAO e no View
            if op == 14: exit()

    def cliente_inserir():
        # id = 0
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        telefone = int(input("Informe seu número de telefone: "))
        # NÃO É NECESSÁRIO CRIAR O OBJETO QUANDO EXISTE O VIEW
        View.cliente_inserir(nome, email, telefone)
    def cliente_listar():
        for obj in View.cliente_listar(): 
            print(obj)     
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        telefone = int(input("Informe o novo número"))
        View.cliente_atualizar(id, nome, email, telefone)
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id a ser excluído: "))
        nome = ""
        email = ""
        telefone = 0
        View.cliente_excluir(id, nome, email, telefone)

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


UI.main()