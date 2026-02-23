#include <iostream>
using namespace std;

class Conta{
    public:
    // Declaração de atributos (obrigatória no C++)
    string titular;
    string numero;
    double saldo;

    // Construtor e Atributos
    Conta(){
        titular = "";
        numero = "";
        saldo = 0;
    }
    void depositar(double valor){
        saldo += valor;
    }
    void sacar(double valor){
        saldo -= valor;
    }
        
};


int main(){
    Conta x; // "x" é uma instância
    cout << x.titular << " " << x.numero << " " << x.saldo << endl;
    x.titular = "Sarah";
    x.numero = "123-p";
    x.saldo = 1000;
    cout << x.titular << " " << x.numero << " " << x.saldo << endl;
    return 0;
}

// C++: tipagem estática
// equivalente ao "self" do Python no C++ = "this"
// void (vazio) = não retorna nada