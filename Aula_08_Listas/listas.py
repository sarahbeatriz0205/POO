x = [] # instância da classe list
y = list() # instância da classe list
z = x # referência à x, não é cópia
w = x[:] # cópia
print(id(x), type(x))
print(id(y), type(y))
print(id(z), type(z))
x.append(10)
y.append(20)
z.append(30) # adicionado à x
print(x)
print(z)
z = [1, 2, 3] # a partir daqui, z agora guarda essa lista
print(z)
