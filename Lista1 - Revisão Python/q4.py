dia = int(input("Insira o dia: "))
mes = int(input("Insira o mês: "))
ano = int(input("Insira o ano: "))

#verificações iniciais
if dia >= 32 or dia <= 1:
    print("Essa data não é válida!")
if mes > 12 or mes < 1:
    print("Essa data não é válida!")
if ano > 2100 or ano < 1900:
    print("Essa data não é válida!")