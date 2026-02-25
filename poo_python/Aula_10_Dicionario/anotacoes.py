x = [] # lista - o que caracteriza: recebe uma sequência de valores e é mutável
y = ()# tupla - o que caracteriza: recebe uma sequência de valores e é imutável (não posso adicionar valores fora a parte)
z = {} # dicionário - o que caracteriza: busca por uma informação pela chave que um valor está associado / o índice é a chave
z = {"RN":"Natal", "PB":"João Pessoa", "PE":"Recife", 1:"Pernambuco"} # não necessariamente a chave precisa ser um texto. pode ser um número
print(z["PE"]) # acessando o valor "Recife" pela a chave "PE"
print(z[1]) # acesso do valor "Pernambuco" pela a chave 1

a = {"RN":"Natal", "PB":"João Pessoa", "PE":"Recife", 1:"Pernambuco"} # dicionário é mutável

# adição de valores em um dicionário
a[2] = "POO"
a[3] = ["TADS", "Redes"] # é possível misturar lista com dicionário e tupla com dicionário dessa maneira
a[4] = "IFRN"
a[5] = ("Macaco", "Planeta")
a[6] = a # guardando ele mesmo = 6:{...}
print(a)

# utiliza apenas as chaves para procurar elementos

b = {2: "POO", 10: "TADS"}
print(max(b))
c = {"2": "POO", "10": "TADS"} # ordem lexicográfica - segue a tabela ASCII e observa qual o código maior na tabela ASCII
print(max(c))