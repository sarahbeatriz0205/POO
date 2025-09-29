class Ingresso:            # entidade - tem instâncias
    def __init__(self, dia, hora):
        self.set_dia(dia)
        self.set_hora(hora)
    def __str__(self): # método especial
        return f"Dia = {self.__dia}, Hora = {self.__hora}"
    def get_dia(self):
        return self.__dia
    def get_hora(self):
        return self.__hora
    
    def set_dia(self, dia): # guarda o dado inserido lá no UI, que aí é o segundo parâmetro (dia) / set: altera o valor do atributo
        # testar o valor dia para armazenar apenas dados validados
        if dia in ["dom" "seg", "ter", "qua", "qui", "sex", "sáb"]:
            self.__dia = dia
        else:
            raise ValueError("Dia Inválido") # quando não for válido, isso é mostrado
    def set_hora(self, hora): # guarda o dado inserido lá no UI, que aí é o segundo parâmetro (hora)
        # testar o valor hora para armazenar apenas os dados validados:
        if hora >= 0 and hora <= 23:
            self.__hora = hora
        else:
            raise ValueError("Hora Inválida")
    