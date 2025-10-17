# Datas, Intervalos e Enumerações
### Módulo datetime
- *Módulo = arquivo importado*
- ***datetime** não tem função, tem apenas classe*
#### Classes do módulo
- **date** – representa uma data com informações de ano, mês e dia
- **time** – representa um horário com dados de horas, minutos, segundos e
microssegundos
- **datetime** – é uma combinação dos tipos date e time
- **timedelta** – intervalo (ou período) de tempo com informações até
microssegundos
- **tzinfo e timezone** - representa as informações de um fuso horário

#### Importação
- **import datetime**: importa todas classes disponíveis do arquivo (programa fica mais pesado e há necessidade de chamar a classe com o nome do módulo)
- **from datetime import "nome_da_classe"**: do módulo *datetime*, importa apenas a classe que você pedir (não há necessidade de chamar a classe com o nomee do módulo)

#### Método de classe
- Um método que eu chamo com a classe
- Exemplos mais comuns: *today* e *now* (retornam o horário do computador)
- **today**: não recebe nenhum parâmetro
- **now**: recebe o fuso horário (se não receber, permanece no padrão)
- **fromisoformat** e **strptime**: transformam uma data que foi passada em string para o formato padrão do datetime
-  **strptime**: método que converte uma string em um datetime;

#### Propriedade
- Não permite que eu ponha um valor diretamente
```
# Forma correta
f = datetime.datetime.strptime("23/06/2023 09:30", "%d/%m/%Y %H:%M")

# Chamando propriedade:
print(f.day)
print(f.month)
print(f.year)
```
```
# Forma incorreta
f = datetime.datetime.strptime("23/06/2023 09:30", "%d/%m/%Y %H:%M")

f.day = 15
```

#### Outras linguagens
- No Java e no C#, por exemplo, o que seria o um módulo no Python, se torna apenas uma classe (ex: math. No Java e no C#, math é classe e o sqrt s torna método)

### Classe timedelta
- Intervalo (ou período) de tempo com informações até
microssegundos
~~~python
from datetime import datetime, timedelta

x = datetime.strptime("10/10/2025 09:00", %d/%m/%Y %H:%M)
y = timedelta(hours=1, minutes=30)
print(x)
print(y)
~~~