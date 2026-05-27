#include <iostream>
using namespace std;

void analizarNumeros(int a, int b, int c, int *sumar, int *mayor, int *menor){ 
    if(sumar == NULL || mayor == NULL || menor == NULL){ // verifica direcciones
    return; 
}
        *sumar = a + b + c;//escribe la suma en la direccion recibida
        
        *mayor = a;// supone inicialmente que a es mayor
        if(b > *mayor){ //compara b con el mayor actual
            *mayor =b; // actualuza el mayor si b es mas grande
        }
        
        if (c > *mayor){//compara c con el mayor actualuza
        *mayor = c; // actualuza el amyor si c es mas grande
        }
        
        *menor = a;//supone inicialmenteque a es el menor
        if (b < *menor){ ///compara b con el menor actualuza
        *menor = b; //actualiza el menor si b es mas pequeño
        }
        
        if(c < *menor){ //compara c con el menor actual
        *menor = c; ///actualiza el menor si c es mas pequeño
}
}
int main() {
        int x = 8; // primera variable original
        int y = 3; // segunda variable original
        int z = 15;// tercer variable original
        
        int sumar;//variable donde se escribira la sumar
        int mayor;//variable donde se escribirael mayor
        int menor;//variable donde se escribira el  menor
        
          
        analizarNumeros(x, y, z, &sumar, &mayor, &menor); //envia valores y direcciones
        cout<<"suma = "<< sumar <<endl; //muestra suma
        cout<<"mayor = "<< mayor <<endl; //muestra el menor
        cout<<"menor = "<< menor <<endl; //// muestra el menor
        

    return 0;
}