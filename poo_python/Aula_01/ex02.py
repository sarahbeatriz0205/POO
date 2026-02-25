#variável, no python, é apenas uma referência para guardar um dado
x = 5
y = 5
z = print #atribui a função print a z
z("Olá")
z = print(z)
print(z)
print(type(x))
print(id(x))
print(id(y))