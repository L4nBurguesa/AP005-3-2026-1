print("=" * 40)
print("   BIENVENIDO AL INVENTARIO")
print("=" * 40)

CATEGORIAS = ("Alimentos", "Bebidas", "Limpieza", "Electrónica", "Otros")

productos = []

def val_num(valor, tipo="float"):
    try:
        if tipo == "float":
            num = float(valor)
        else:
            num = int(valor)
        if num >= 0:
            return num
        else:
            print("El valor debe ser mayor o igual a cero.")
            return None
    except ValueError:
        print("Debes ingresar un número válido.")
        return None

def val_categoria(categoria):
    if categoria in CATEGORIAS:
        return True
    else:
        print(f"Categoría no válida. Permitidas: {CATEGORIAS}")
        return False

def cod_existe(codigo):
    for producto in productos:
        if producto["codigo"] == codigo:
            return True
    return False

def agregar_prod():
    print("\n----AGREGAR PRODUCTO----")
    while True:
        codigo = input("Código: ").strip()
        if codigo == "":
            print("El código no puede estar vacío.")
            continue
        if cod_existe(codigo):
            print("Ya existe un producto con ese código. Usa otro.")
        else:
            break

    nombre = input("Nombre: ").strip()
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre: ").strip()

    while True:
        precio_str = input("Precio: ")
        precio = val_num(precio_str, "float")
        if precio is not None:
            break

    while True:
        cant_str = input("Cantidad: ")
        cantidad = val_num(cant_str, "int")
        if cantidad is not None:
            break

    print(f"Categorías permitidas: {CATEGORIAS}")
    while True:
        categoria = input("Categoría: ").strip()
        if val_categoria(categoria):
            break

    producto = {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "categoria": categoria
    }
    productos.append(producto)
    print("Producto agregado exitosamente.")

def mostrar_prod():
    if not productos:
        print("No hay productos registrados.")
        return

    print("\n----LISTA DE PRODUCTOS----")

    for idx, prod in enumerate(productos, start=1):
        print(f"\nProducto #{idx}")
        print(f"  Código   : {prod['codigo']}")
        print(f"  Nombre   : {prod['nombre']}")
        print(f"  Precio   : ${prod['precio']:.2f}")
        print(f"  Cantidad : {prod['cantidad']}")
        print(f"  Categoría: {prod['categoria']}")
        total_inventario = 0
        for prod in productos:
            total_inventario +- prod['precio']*prod['cantidad']
            print(f"Valor total del inventario: ${total_inventario:.2f}")
    print("-" * 30)

def buscar_prod():
    if not productos:
        print("No hay productos registrados.")
        return
    print("\n----BUSCAR PRODUCTO----")
    criterio = input("Buscar por (código / nombre): ").strip().lower()
    if criterio not in ("codigo", "nombre"):
        print("Criterio no válido. Usa 'código' o 'nombre'.")
        return
    busqueda = input("Buscar: ").strip().lower()
    encontrados = []
    for prod in productos:
        if criterio == "codigo" and prod["codigo"].lower() == busqueda:
            encontrados.append(prod)
        elif criterio == "nombre" and busqueda in prod["nombre"].lower():
            encontrados.append(prod)
    if encontrados:
        print(f"Resultados ({len(encontrados)} encontrado(s)):")
        for prod in encontrados:
            print(f"Código: {prod['codigo']} | Nombre: {prod['nombre']} | Precio: ${prod['precio']:.2f} | Cant: {prod['cantidad']} | Cat: {prod['categoria']}")
    else:
        print("No se encontraron productos.")

def eliminar_prod():
    if not productos:
        print("No hay productos registrados.")
        return
    print("\n----ELIMINAR PRODUCTO----")
    codigo = input("Código del producto a eliminar: ").strip()
    for i, prod in enumerate(productos):
        if prod["codigo"] == codigo:
            confirmar = input(f"¿Eliminar '{prod['nombre']}'? (s/n): ").strip().lower()
            if confirmar == "s":
                del productos[i]
                print("Producto eliminado.")
            else:
                print("Eliminación cancelada.")
            return
    print("Producto no encontrado.")

while True:
    print("\n" + "=" * 40)
    print("          MENÚ PRINCIPAL")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")
    print("=" * 40)

    opcion = input("Selecciona una opción (1-5): ").strip()

    if opcion == "1":
        agregar_prod()
    elif opcion == "2":
        mostrar_prod()
    elif opcion == "3":
        buscar_prod()
    elif opcion == "4":
        eliminar_prod()
    elif opcion == "5":
        print("\n Fin del sistema.")
        break
    else:
        print("Opción no válida. Elige 1, 2, 3, 4 o 5.")