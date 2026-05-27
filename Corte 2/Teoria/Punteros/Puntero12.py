#include <iostream>
using namespace std;

int main() {
        int *p = NULL; // el puntero se inicia en NULL porque aun no apunta aun int
        
        if(p != NULL){ /// solo se desreferencia si apunta a una diereccion valida
        
        cout<<"valor = "<<*p<<endl;
        } else {
            
            cout<<"p no apunta a una direccion valida"<<endl;
        }

    return 0;
}