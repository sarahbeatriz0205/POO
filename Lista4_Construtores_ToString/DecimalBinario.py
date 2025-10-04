class DecimalBinario:
    def __init__(self, decimal):
        self.__decimal = decimal

        if decimal >= 0:
            self.__decimal = decimal
        else:
            raise ValueError()
        
    def set_decimal(self, num):
        if num >= 0:
            self.__decimal = num
        else:
            raise ValueError()
    
    def get_decimal(self):
        return self.__decimal

    def __str__(self):
        return f"Em decimal: {self.__decimal} \nEm binário: {bin(self.__decimal)[2:]}"
    
# [2:] inicie a impressão a partir do índice 2