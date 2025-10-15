import json
class Cliente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
    def __str__(self):
        return f"{self.nome} - {self.id}"

a = Cliente(1, "Douglas")
b = Cliente(2, "Sarah")
c = Cliente(3, "Julian")
print(vars(a))
clientes = [a, b, c]

with open("clientes.json", mode="w") as arquivo:
    json.dump(clientes, arquivo, default = vars)