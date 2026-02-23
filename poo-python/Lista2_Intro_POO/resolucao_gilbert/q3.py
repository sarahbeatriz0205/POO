class Conta:
    def __init__(self): # __init__: Construtor
        # Atributos
        self.titular = "" # para inserir string (texto)
        self.numero_conta = "" # para inserir string (texto)
        self.saldo = 0
    def depositar(self, valor):
        self.saldo += valor
    def sacar(self, valor):
        self.saldo -= valor


class UI:
    def main():
        x = Conta()
        print(x.titular, x.numero_conta, x.saldo) # antes da atualização
        x.titular = "Sarah"
        x.numero_conta = "123-x"
        x.saldo = 1000
        x.depositar(500) # por baixo dos panos: self = x = Conta()     Conta.depositar(x, 500)
        print(x.titular, x.numero_conta, x.saldo) # depois da atualização

        z = x # "z" é apenas referência para a mesma instância de "x"
        contas = [x] # outra referência para a mesma instância de "x"
        contas[0].depositar(500)

# Python = tipagem dinâmica