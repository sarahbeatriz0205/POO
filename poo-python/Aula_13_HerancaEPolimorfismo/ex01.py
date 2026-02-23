from abc import ABC, abstractmethod # ABC: Abstract Class Method -> importação particular do Python

class ClasseBase:
    pass
class ClasseDerivada(ClasseBase): # (ClasseBase) - indica que a ClasseDerivada herda de ClasseBase
    pass
# O construtor da ClasseBase não é herdado, mas você pode chamá-lo


class Mamifero: # classe abstrata, pois não é possível instanciá-la puramente
    @abstractmethod
    def emitir_som(self): # método abstrato. ainda não tem funcionalidade, mas é previsto que ela seja utilizada em classes descendentes. quando utilizadas, podem e devem ser mudadas com polimorfismo
        pass
class Gato(Mamifero):
     # está sendo possível a utilização desse método porque a classe Gato está herdando tudo da classe Mamifero
     def emitir_som(self): # Polimorfismo: alterar algo que foi herdado, uma instrução. Alteração feita de acordo com a necessidade e o contexto
        return "Miau"
class Cachorro(Mamifero): 
    def emitir_som(self):
        return "Auau"

x = Gato()
y = Cachorro()
print(type(x)) # type: testa especificamente o tipo do objeto (<class '__main__.Gato>)
print(isinstance(x, Gato)) # insinstance: verifica se um objeto é instância de uma determinada classe ancestral
print(isinstance(x, Mamifero)) # True
print(isinstance(x, ClasseBase)) # False
print(issubclass(Gato, object)) # todas as classes já herdam de uma classe chamada Object

# classe Object fornece para a minha classe:
#| Método      | Função                  |
#| ----------- | ----------------------- |
#| `__init__`  | Inicialização do objeto |
#| `__str__`   | Representação em string |
#| `__repr__`  | Representação oficial   |
#| `__eq__`    | Comparação (`==`)       |
#| `__hash__`  | Hash do objeto          |
#| `__class__` | Classe do objeto        |

print(x.emitir_som()) # emitir_som do objeto Gato()
print(y.emitir_som()) # emitir_som do objeto Cachorro()