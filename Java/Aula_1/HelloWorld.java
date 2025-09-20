class HelloWorld{ //todo código em Java deve estar dentro de uma classe (extremamente orientada à objetos)
    public static void main (String[] args){ // método principal, pertencente à classe HelloWorld
        System.out.print("Hello, World!");
    }
}


// Explicação de cada parte do código acima:

// class HelloWorld: cria uma classe chamada HelloWorld (é obrigatório que o nome do arquivo e o nome da classe sejam iguais)

// public static void main: método principal do programa, onde a execução começa
    // public: significa que esse método pode ser acessado de qualquer lugar do código
    // static: define esse método como pertencente à classe HelloWorld. define também que esse método pode ser acessado sem a necessidade de criar um objeto "new"
    // void: o método não retorna nenhum valor. ele executa uma série de instruções, mas não produz um resultado que possa ser usado ou armazenado por outra parte do programa
    // main: nome do método
    // String[] args: Um array de strings que pode ser usado para passar argumentos de linha de comando para o programa

// System.out.println("Hello World!"): imprime a mensagem
    // System: Uma classe que contém campos e métodos úteis para interagir com o sistema, como o console
    // out (Output Stream): um objeto de fluxo de saída da classe System
    // print: Um método do objeto out que imprime uma linha de texto no console
        // println: Um método do objeto out que imprime uma linha de texto no console, mas indica que após a 1ª linha, virá outra linha