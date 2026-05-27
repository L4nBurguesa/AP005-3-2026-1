#include <iostream> // Biblioteca para entrada y salida en C++

using namespace std;

void intercambiar(int a, int b){ // a y b son copias locales
    int temp = a; // guarda temporalmente el valor en Antes
    a = b; // cambia la copia a
    b = temp; //cambia la copia b
    
    cout <<"dentro de intercambiar: a = "<< a <<", b = "<< b <<endl;
    }
    
int main() { // Función principal del programa

    int x = 10; // primera Variable original
    int y = 20; //segunda Variable original
    
    cout << "Antes: x = " << x <<", y = "<< y << endl;//valores antes del intercambio
    
    intercambiar(x,y); //envia valores del intercambio

    cout << "Despues: x = " << x <<", y = " << y <<endl; // x no cambia porque solo se modifico la copia
    
    return 0; // Finalización exitosa del programa
}