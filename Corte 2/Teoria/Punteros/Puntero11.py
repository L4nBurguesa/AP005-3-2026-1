#include <iostream>
using namespace std;

int main() {
        int datos[3] = {10,20, 30}; // arreglo 3 enteros
        int *p = datos; // p apunta al primer elemento del arreglo
        
        
        cout<<"datos[0] = "<<datos[0] <<endl; //acceso mediante indice
        cout<<"*p = "<< *p <<endl; //acceso mediante el puntero
        cout<<"*(p + 1) = "<< *(p + 1) <<endl; //// accesoal segundo ellementp
        cout<<"*(p + 2) = "<< *(p + 2 )<<endl; // acceso tercer elemento
        

    return 0;
}