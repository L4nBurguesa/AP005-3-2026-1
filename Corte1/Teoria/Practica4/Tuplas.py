# LISTAS 

colores = ["Rojo", "Azul", "Amarillo", "Naranja", "Violeta", "Verde"]

print("Lista original:", colores)
print("Tamaño:", len(colores)) #tamaño de la lista
print("Tercer elemento:", colores[2]) #imprime la posicion 2

colores.append("Blanco") #agrga color
colores.insert(3, "Negro") # inserta en la posicion 3
colores += ["Marron", "Gris"] # agrega dos colores a la vez

print("\nLista actualizada:", colores) #imprime tupla

colores.remove("Marron") #quita marron

colores.sort() # organiza orden alfabetico
print("Lista ordenada:", colores)

#TUPLAS 

tupla_colores = tuple(colores) #convierte lista en tupla
print("\nTupla:", tupla_colores)

print("¿Está 'Rojo' en la tupla?", "Rojo" in tupla_colores)#busca rojo en la tupla

tupla_unica = ("Blanco",)
print("Tupla con un elemento:", tupla_unica)

datos = ("Gaspar", 5, 8, 1999)
nombre, dia, mes, año = datos

print("\nNombre:", nombre)
print("Fecha:", dia, "/", mes, "/", año)

lista_datos = list(datos)
print("Tupla convertida en lista:", lista_datos) #convierte tupla en lista