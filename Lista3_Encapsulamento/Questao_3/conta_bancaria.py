class Conta:
    def __init__(self, nome, num_conta, deposito, saque):
        self.set_nome(nome)
        self.set_num_conta(num_conta)
        self.__saldo = 1000
        self.set_deposito(deposito)
        self.set_saque(saque)
        
    def get_nome(self):
        return self.__nome
    def get_num_conta(self):
        return self.__num_conta
    def get_saldo(self):
        return self.__saldo
    def get_deposito(self):
        return self.__deposito
    def get_saque(self):
        return self.__saque

    def set_nome(self, nome):
        self.__nome = nome
    def set_num_conta(self, num_conta):
        self.__num_conta = num_conta
    def set_deposito(self, deposito):
        if deposito > 1:
            self.__deposito + self.__saldo
        else:
            raise ValueError("Ocorreu um erro! O valor deve ser maior que 1")
    def set_saque(self, saque):
        if saque < self.__saldo:
            self.__saldo - self.__saque
        else:
            raise ValueError("Ocorreu um erro! Você não tem saldo o suficiente!")
    
    def deposito(self, deposito):
        valor = deposito
        return self.__saldo + valor
    def saque(self, saque):
        return self.__saldo - saque