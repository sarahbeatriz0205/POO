public abstract class Animal{ // superclasse
    public abstract void emitir_som(); // método abstrato
    }

public class Cachorro extends Animal{ // extends: indica que a classe Cachorro herda da classe Animal
    public void emitir_som(){
        System.out.println("AuAu"); // Polimorfismo: mudança de acordo com o contexto
    }
}

public class Gato extends Animal{
    public void emitir_som(){
        System.out.println("Miau");
    }
}

public class Main{
    public static void main(String[] args) {
        Animal gato = new Gato();
        Animal cachorro = new Cachorro();

        a1.emitir_som();
        a2.emitir_som();
    }
}