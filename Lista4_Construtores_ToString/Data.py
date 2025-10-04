class Data:
    def __init__(self, d, m, a):
        # Validação dos dias
        if d > 0 and d < 32:
            self.__dia = d
        else:
            raise ValueError()
        # Validação do mês
        if m > 0 and m < 13:
            self.__mes = m
        else:
            raise ValueError()
        if a > 999 and a <= 9999:
            self.__ano = a
        else:
            raise ValueError()
        
    def set_dia(self, d):
        if d > 0 and d < 32:
            self.__dia = d
        else: 
            raise ValueError()
    def set_mes(self, m):
        if m > 0 and m < 13:
            self.__mes = m
        else:
            raise ValueError()
    def set_ano(self, a):
        if a > 999 and a <= 9999:
            self.__ano = a
        else:
            raise ValueError()

    def get_dia(self):
        return self.__dia
    def get_mes(self):
        return self.__mes
    def get_ano(self):
        return self.__ano

    def __str__(self):
        return f"{self.__dia:02d}/{self.__mes:02d}/{self.__ano}"