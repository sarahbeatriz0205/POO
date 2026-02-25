package poo_java.estudos;

public class ContaBancaria{
    public String nome;
    public double saldo;

    public void abreContaComDepositoImediato(String nome, double deposito){
        this.nome = nome;
        this.saldo = deposito;
    }

    public void abreContaSimples(String nome){
        this.nome = nome;
        this.saldo = 0.00;
        System.out.println("Conta criada com sucesso!");
    }

    public void depositar(double dinheiro_depositado){
        this.saldo += dinheiro_depositado;
        System.out.println("Valor depositado com sucesso!");
    }

    public void retirar(double dinheiro_retirado){
        if (dinheiro_retirado > this.saldo){
            System.out.println("Erro! Seu saldo está negativo.");
            System.out.println("Valor atual " + this.saldo);
        }
        else{
            this.saldo -= dinheiro_retirado;
            System.out.println("Dinheiro retirado com sucesso!");
            System.out.println("Valor atual " + this.saldo);
        }
    }
    
    public void mostrarDados(){
        System.out.println("Nome do usuário: " + this.nome);
        System.out.println("Saldo atual " + this.saldo);
    }
}