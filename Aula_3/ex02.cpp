#include <iostream>
using namespace std;

int main(){
    // diferente do python, as duas variáveis que referenciam o número 5 estão sendo referência para diferentes espaços de memória
    // & = endereço
    int x = 5;
    int y = 5;
    int z = 10;

    // ponteiro: aponta para onde uma variável está armazenada
    // obs: ponteiro: todas as variáveis são ponteiros
    // a variável, no c++, guarda instância
    int *p = &x; // guarda o ENDEREÇO de "x" no endereço de "p"
    cout << x << " " << &x << endl;
    cout << y << " " << &y << endl;
    cout << z << " " << &z << endl;

    // mostra o que "p" armazena, o endereço onde "p" está armazenado e mostra o valor que está armazenado no endereço que "p" está armazenando
    cout << p << " " << &p << " " << (*p) << endl;
    return 0;
}