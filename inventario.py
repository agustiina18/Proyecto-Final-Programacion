import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   codigo TEXT UNIQUE NOT NULL,
                   nombre TEXT NOT NULL, 
                   descripcion TEXT NULL, 
                   cantidad INTEGER NOT NULL, 
                   precio REAL NOT NULL, 
                   categoria TEXT 
                   )''')
    conexion.commit()
    conexion.close()


def menu_principal():
    while True:
        print("\nMenu Principal")
        print("1. Registrar producto")
        print("2. Visualizar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Buscar producto")
        print("6. Reporte de bajo stock")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            visualizar_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            buscar_producto()
        elif opcion == '6':
            reporte_bajo_stock()
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


def registrar_producto():
        codigo = input("Ingrese el codigo del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese una descripcion: ")
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio: "))
        categoria = input("Ingrese la categoria: ")

        #Conectar a la base de datos 
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        #Insertar el producto de la tabla
        cursor.execute('''
                       INSERT INTO productos (codigo, nombre, descripcion, cantidad, precio, categoria) 
                       VALUES (?, ?, ?, ?, ?, ?)''',
                       (codigo, nombre, descripcion, cantidad, precio, categoria))
        
        #Guardar los cambios y cerrar la conexion
        conexion.commit()
        conexion.close()
        
        print("Producto registrado con exito.")


def visualizar_productos():
        #Conectar a la base de datos
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        #Obtener los productos de la tabla
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

        #Mostrar los productos
        if productos:
            print("\nInventario de Productos")
            print("ID / Codigo / Nombre / Descripcion / Cantidad / Precio  Categoria")
            print("-" * 70)
            for producto in productos:
                print(f"{producto[0]} / {producto[1]} / {producto[2]} / {producto[3]} / {producto[4]} / {producto[5]} / {producto[6]}")
        else:
            print("No hay productos registrados.")

        conexion.close()

crear_base_datos()
registrar_producto()
visualizar_productos()

def actualizar_producto():
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))

        #Conectar a la base de datos
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        #Actualizar la cantidad del producto
        cursor.execute("UPDATE productos SET cantidad = ? WHERE id = ?", (nueva_cantidad, id_producto))

        #Guardar los cambios 
        conexion.commit()
        conexion.close()
        
        print("Producto actualizado con exito.")


def eliminar_producto():
        id_producto = int(input("Ingrese el ID del producto a eliminar: "))

        #Conectar a la base de datos
        conexion = sqlite3.connect("inventario.db")
        cursor = conexion.cursor()

        #Eliminar el producto de la tabla
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))

        #Guardar los cambios
        conexion.commit()
        conexion.close()
        
        print("Producto eliminado con exito.")


def buscar_producto():
    print("\nOpciones de búsqueda:")
    print("1. Buscar por ID")
    print("2. Buscar por nombre")
    print("3. Buscar por categoría")
    opcion = input("Seleccione una opción: ")
    
    # Conectar a la base de datos
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    
    if opcion == '1':
            id_producto = int(input("Ingrese el ID del producto: "))
            cursor.execute('SELECT * FROM productos WHERE id = ?', (id_producto,))
    elif opcion == '2':
            nombre_producto = input("Ingrese el nombre del producto: ")
            cursor.execute('SELECT * FROM productos WHERE nombre LIKE ?', (f'%{nombre_producto}%',))
    elif opcion == '3':
            categoria_producto = input("Ingrese la categoría: ")
            cursor.execute('SELECT * FROM productos WHERE categoria LIKE ?', (f'%{categoria_producto}%',))
    else:
        print("Opción no válida.")
        return

    resultados = cursor.fetchall()

    if resultados:
        print("\nResultados de búsqueda:")
        print("ID | Código | Nombre | Descripción | Cantidad | Precio | Categoría")
        print("-" * 70)
        for producto in resultados:
            print(f"{producto[0]} / {producto[1]} / {producto[2]} / {producto[3]} / {producto[4]} / {producto[5]} / {producto[6]}")
    else:
        print("Producto no encontrado.")

    conexion.close()


def reporte_bajo_stock():
    limite = int(input("Ingrese la cantidad limite para el reporte: "))

    #Conectar a la base de datos
    conexion = sqlite3.connect("inventario.db")
    cursor = conexion.cursor()

    #Obtener los productos con bajo stock
    cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
    productos = cursor.fetchall()

    if productos:
        print("\nReporte Bajo Stock")
        print("ID / Codigo / Nombre / Cantidad")
        print("-" * 40)
        for prod in productos:
            print(f"{prod[0]} / {prod[1]} / {prod[2]} / {prod[4]}")
    else:
        print("No hay productos con bajo stock.")

    conexion.close()
