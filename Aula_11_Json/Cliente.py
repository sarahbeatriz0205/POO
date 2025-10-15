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

# Maneiras de organizar os dados em um JSON
# Abertura de arquivos

# Salva a lista clientes em um json
# mode="w" -> cria o arquivo e escreve o que você mandou
with open("clientes.json", mode="w") as arquivo: # with serve para fechar o arquivo; open("clientes.json", mode="w") as arquivo diz que o arquivo deve ser aberto como variável arquivo
    json.dump(clientes, arquivo, default = vars)

arquivo = open("clientes.json", mode="w")
json.dump(clientes, arquivo, default=vars, indent=4)
arquivo.close()