class Ingresso:            # entidade - tem instâncias
    def __init__(self):
        self.dia = "dom"   # definição dos atributos
        self.hora = 17
    
    # Validação de dados está na entidade
    def get_dia(self): # get: retorna o valor atual do atributo
        return self.__dia # seguido de __, ele "esconde" certo dado, está encapsulado
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
    
    def inteira(self):
        if self.__dia == "qua": return 8
        if self.__dia in ["seg", "ter", "qui"]: valor = 16
        else: valor = 20
        if self.__hora == 0 or self.hora >= 17: valor *= 1.5
        return valor    

# Exemplo - Estado, Comportamento e Identidade:  
x = Ingresso()
y = Ingresso()
print(id(x))
print(id(y))
# x e y estão no mesmo estado por enquanto, dados não mudaram
# x e y, no entanto, possuem identidades diferentes na memória, criadas a partir do momento em que Ingresso() foi atribuído a x e y