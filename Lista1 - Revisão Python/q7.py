# tentativa falha
frase = (input("Digite uma frase: ").split())
for i in range(len(frase)):
    frase.remove(frase[i])
    print(frase)