class Venda:
    def __init__(self, id, data, idCliente):
        self.id = id
        self.data = data
        self.carrinho = True
        self.total = 0
        self.idCliente = idCliente