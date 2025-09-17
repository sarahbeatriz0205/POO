data = input("Digite a data: ")
d, m, a = map(int, data.split("/"))
max_d = 31
if m in [4, 6, 9, 11]:
    max_d = 30
if m == 2:
    if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
        max_d = 29
    else:
        max_d = 28
if 1 <= d <= max_d and 1 <= m <= 12:
    print("Data válida!")
else:
    print("Data inválida!")