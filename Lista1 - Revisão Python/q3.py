numbers = list(map(int, input().split()))
numbers.sort()
maior = numbers[3]
menor = numbers[0]

for i in range(len(numbers)):
    if numbers[i] == numbers[i - 1]:
        print("Erro!")
        exit() #responsável por parar o programa
print("Maior valor =", maior, "\nMenor valor =", menor, "\nA soma do segundo maior valor com o segundo menor valor =", numbers[2] + numbers[1])
        