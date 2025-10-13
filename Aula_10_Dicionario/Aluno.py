class Aluno:
    def __init__(self, nome, matricula, idade):
        self.nome = nome
        self.matricula = matricula
        self.idade = idade

a = Aluno("Raquel", "20251014040000", 19)
b = Aluno("Miguel", "20251014040001", 18)

# transforma as informações recebidas em um dicionário
# os nomes dos atributos se tornam o nome das chaves (em string)
#print(a.__dict__)
#print(b.__dict__)
#print(vars(b)) # A função vars() em Python retorna o atributo __dict__ de um objeto

# retorna uma tupla com os valores e ao lado retorna o tipo do dado - <class 'tuple'>
b = vars(b)
for item in b.items():
    print(item, type(item))