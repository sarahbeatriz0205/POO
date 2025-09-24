class Ingresso: #Entidade: tem instâncias
    def __init__(self):
        self.dia = ""
        self.horario = 0
    def ingresso_inteira(self):
        if self.dia == "qua":
            return 8
        if self.dia in ["seg", "ter", "qui"]:
            valor = 16
        else:
            valor = 20
        if self.hora == 0 or self.hora >= 17:
            valor = valor * 1.5
        return valor
    def meia(self):
        if self.dia == "qua":
            return self.ingresso_inteira() / 2