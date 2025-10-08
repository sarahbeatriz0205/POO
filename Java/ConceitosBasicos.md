### Instanciação de um objeto
~~~java
// Java e C#

Carro x  = new Carro();
// Carro: tipo definido na classe (obrigatório que a referência tenha um tipo)
// x: referência para a nova instância
// new Carro(): aloca em um novo espaço na memória e cria essa nova instância
// Mesma coisa no C#
~~~
~~~c++
// C++

Carro *x = new Carro();
// Mesma coisa do Java e do C#, mas em vez de utilizar referências, utiliza ponteiros para locais da memória
// Obrigatório que o ponteiro tenha um tipo
~~~
~~~python
# Python

x = Carro()
~~~
~~~ruby
# Ruby

x = Carro.new
# .new é um método no Ruby
~~~

### Comunicação entre objetos
- Chamada de método (envio de mensagens);

- O destinatário verifica se ele tem um método com o nome da mensagem;

### Abstração
- Objetos representam coisas do mundo real e computacional;
- Abstrai as coisas importantes que fazem algo funcionar. A classe é uma abstração;
- Abstrai o usuário da maneira como aquilo funciona "por debaixo dos panos", pois ele só quer saber se irá resolver o problema dele;
- O que o usuário precisa saber (Abstração): Ele precisa saber que existe um pedal para acelerar e um pedal para frear. Ele se importa com a interface (os pedais e o volante).
- O que a Abstração esconde (Implementação Complexa): O usuário não precisa saber como a injeção eletrônica funciona, a taxa de compressão do motor ou a dinâmica de fluidos no sistema de freios. Esses são detalhes internos que seriam complexos e irrelevantes para a tarefa de dirigir.

- Na POO, **um método como carro.acelerar() é a abstração**. O código dentro desse método pode ser centenas de linhas complexas, mas para o usuário que está usando o objeto carro, basta saber que chamar o método fará o carro ir mais rápido.