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

clientes = [a, b, c]

# Abrindo e acessando o arquivo
# mode="r" -> ler o arquivo, ver o que tem nele
with open("clientes.json", mode="r") as arquivo:
    list_dic = json.load(arquivo) # abrindo o json
    for dic in list_dic:
        c = Cliente(dic["id"], dic["nome"])
        clientes.append(c)
for c in clientes:
    print(c)