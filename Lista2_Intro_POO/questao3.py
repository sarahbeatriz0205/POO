class Conta_Bancaria:
    def __init__(self, nome_cliente):
        self.nome_cliente = nome_cliente
        self.numero_conta = 0
        self.saldo_disponivel = 1200.0
    def depositar(self, valor_deposito):
        if valor_deposito > 0:
            d = valor_deposito + self.saldo_disponivel
        else:
            print("Erro! O valor deve ser maior que 0!")
            exit()
        return d
    def sacar(self, valor_saque):
        if valor_saque > self.saldo_disponivel:
            print("Erro! Saldo insuficiente.")
            exit()
        else:
            s = self.saldo_disponivel - valor_saque
        return s


x = Conta_Bancaria(input("Insira seu nome completo: "))
x.numero_conta = int(input("Digite o número da sua conta: "))
sim_ou_nao_deposito = input("Deseja depositar algum valor?")
if sim_ou_nao_deposito == "Sim":
    valor_deposito = float(input("Insira o valor que deseja depositar: "))
    print("Parabéns! O seu saldo atual é de R$", x.depositar(valor_deposito))
else:
    sim_ou_nao_saque = input("Deseja sacar algum valor?")
    if sim_ou_nao_saque == "Sim":
        valor_saque = float(input("Insira o valor a ser sacado: "))
        print("O seu valor atual é de R$:", x.sacar(valor_saque))
    else:
        print("Ok! O valor do seu saldo é de R$ ", x.saldo_disponivel)