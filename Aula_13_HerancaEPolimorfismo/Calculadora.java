public class Calculadora{
    public int somar(int a, int b){
        return a + b;
    }

    public int somar(int a, int b, int c){
        return a + b + c;
    }
}

public class Main{
    public static void main(String[] args){
        Calculadora n = new Calculadora();
        System.out.println(n.somar(2, 3));    
        System.out.println(n.somar(2, 3, 4));
    }
}