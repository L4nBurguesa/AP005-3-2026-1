#include <iostream> // Biblioteca para entrada y salida
#include <cstddef>  // Biblioteca donde está NULL

using namespace std;

// p recibe una copia de una dirección
void cambiar(int* p) {

    // Verifica si el puntero es válido
    if (p == NULL) {
        return; // Sale para evitar errores
    }

    // Cambia el valor almacenado en la dirección apuntada
    *p = 100;
}

int main() {

    int x = 5; // Variable original

    cout << "Antes: x = " << x << endl;

    cambiar(&x); // Se envía la dirección de x

    cout << "Despues: x = " << x << endl;

    return 0;
}