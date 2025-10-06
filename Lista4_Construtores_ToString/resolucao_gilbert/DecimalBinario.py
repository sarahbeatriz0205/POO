class Conversor:
    def __init__(self, num):
        self.set_num(num)
    def set_num(self, num):
        self.__num = num
    def get_num(self):
        return self.__num
    
    # menos eficiente, tem mais operações
    def binario(self):
        restos = []
        n = self.__num
        while n > 0:
            restos.append(n%2) # push -> coloca na pilha
            n = n // 2
        bin = ""
        while len(restos) > 0:
            bin = bin + str(restos.pop()) # pop -> esvazia a pilha
        return bin
    
    # mais eficiente
    def binario2(self):
        bin = ""
        n = self.__num
        while n > 0:
            bin = str(n % 2) + bin
            n = n // 2
        return bin
    def __str__(self):
        return f"Decimal: {self.__num} \nBinário: {x.binario()} \nBinário2: {x.binario2()}"

x = Conversor(14)
print(x)