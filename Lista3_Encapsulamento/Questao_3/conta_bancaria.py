class ContaBancaria:
    def __init__(self, nome, numeroConta, senha):
        self.__nome = nome
        self.__numeroConta = numeroConta
        self.__senha = senha
        self.saldo = float(10.55)

    # retorna os valores desses atributos antes e depois da modificação
    def get_nome(self):
        return self.__nome
    def get_numeroConta(self):
        return self.__numeroConta
    def get_senha(self):
        return self.__senha
    
    # altera e valida os valores
    def set_nome(self, newNome):
        if newNome == "":
            return "Erro! O campo deve ser preenchido!"
            exit()
        else:
            self.__nome = newNome
    def set_numeroConta(self, newNumeroConta):
        if newNumeroConta == "":
            return "Erro! O campo deve ser preenchido!"
            exit()
        self.__numeroConta = newNumeroConta
    def set_senha(self, newSenha):
        if newSenha == "":
            return "Erro! O campo deve ser preenchido!"
            exit()
        else:
            self.__senha = newSenha
            

    # tentar "validar" o acesso lá no menu 
    def deposito(self, valorDeposito):
            if valorDeposito > 0:
                self.saldo = self.saldo + valorDeposito
                return f"Valor depositado com sucesso! Seu saldo agora é de R$ {self.saldo:.2f}"
            else:
                return "Tá querendo depositar o vento, é? O valor tem que ser maior que 0, meu chapa."

    def saque(self, valorSaque):
        if valorSaque > self.saldo:
            return "Vai tirar essa grana daqui? Vai não, viu. Você não tem saldo suficiente KKKKKKKKKKKKKKK"
        else:
            self.saldo = self.saldo - valorSaque
            return f"Valor sacado com sucesso! Seu saldo agora é de R$  {self.saldo:.2f}"