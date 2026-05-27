#include <iostream>
using namespace std;

void intercambiar(int *a, int *b){ //a y b reciben direcciones de variables reinterpret_cast
    if(a == NULL || b == NULL){ // verifica si alguna direccion no es valida
    return; 
}
        int temp = *a;//guarda el contenido apuntado por apuntado
        *a = *b; // escribe en la direccion apuntada por a el contenido apuntado por b
        *b = temp; // escribe en la direccion apuntada por b el valor temporal

}

int main()
{
        int x = 10; // primera variable original
        int y = 20; // segunda variable original
        
        
        cout<<"Antes: x = "<<x<<", y = "<<y<<endl; //variables antes del intercambio  
        intercambiar(&x,&y); //envia las direcciones x e dynamic_cast
        cout<<"despues: x = "<<x<<", y = "<<y<<endl; //ahora las variables originales cambiaron
        

    return 0;
}