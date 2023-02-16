#creamos una lista vacia para almacernar la compras

compras = []

#creamos un bucle para las opciones de agregar al final, eliminar el inicio, y mostrar en la lista el orden de las compras

while True:
    opcion = input("""  Ingresa una opcion: 
    >> 1.- agregar un producto 
    >> 2.- eliminar un producto
    >> 3.- mostrar la lista
    >> 4.- salir: 
    >> """)
    
    #agregar al inicio de la lista
    if opcion.upper() == '1':
        producto = input("Ingresa el nombre del producto: ") #nos pide ingresar el nombre del producto
        compras.append(producto)
        print(f"Producto '{producto}' agregado a la lista.")

    #Eliminar el producto inicial de nuestra lista de compras
    elif opcion.upper() == '2':
        if len(compras) == 0: #si la longitud de la lista es 0 osea no tiene ningun elemento imprimira lo siguiente
            print("La lista de compras está vacía.")
        else:
            producto_eliminado = compras.pop(0) # pop elimina el ultimo elemento de la lista e imprimira lo siguiente
            print(f"Producto '{producto_eliminado}' eliminado de la lista.")

    # mostrar la lista
    elif opcion.upper() == '3':
        if len(compras) == 0: #si la longitud de la lista es 0 osea no tiene ningun elemento imprimira lo siguiente
            print("La lista de compras está vacía.")
        else:
            print("Lista de compras:")
            for i, producto in enumerate(compras): #enumerate hace que cada item de la lista quede enumerado y ya no imprire la lista tal cual entre corchetes
                print(f"{i+1}. {producto}") # de lo anterior imprimre cada producto en una lista en lines continuas

    # salir del programa
    elif opcion.upper() == '4':
        print("Gracias! Vuelva Pronto.")
        break #sale del bucle
    else:
        print("Opción inválida. Por favor intenta de nuevo.") #si se ingresa un opcion erronea te vuelve a mostrar la lista de opciones