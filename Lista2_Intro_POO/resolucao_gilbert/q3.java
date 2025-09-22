class Conta {
    public String titular;
    public String numero;
    public double saldo;
    public Conta(){
        titular = "";
        numero = "";
        saldo = 0;
    }
    public void depositar(double valor){
        saldo += valor;
    }
    public void sacar(double valor){
        saldo -= valor;
    }
}

public class q3 {
    public static void main(String[] args) {
        Conta x = new Conta();
        System.out.println(x.titular + " " + x.numero + " " + x.saldo);
        x.titular = "Sarah";
        x.numero = "123-x";
        x.saldo = 1000;
        System.out.println(x.titular + " " + x.numero + " " + x.saldo);
        x.depositar(500);
        System.out.println(x.titular + " " + x.numero + " " + x.saldo);
    }
}