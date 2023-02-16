
#creamos una lista vacia que almacene nuestras tareas pendientes

tareas_pendientes = []

#creamos un bucle para las opciones de agregar al final, eliminar el inicio, y mostrar en la lista el orden de las compras
while True:
    opcion = input("""Ingresaa una opcion: 
    >>1.- agregar una tarea
    >>2.- elminar una tarea
    >>3.- mostrar la lista
    >>4.- contar las tareas 
    >>5.- salir: 
    >> """)

    #para crear y agregar una tarea
    if opcion.upper() == "1":
        tarea = input("Ingresa la tarea: ") 
        tareas_pendientes.insert(0, tarea)  #agrega la tarea al incio de la lista
        print(f"Tarea '{tarea}' agregada al inicio de la lista.")

    #para eliminar una tarea de la lista de tarea
    elif opcion.upper() == "2":
        if len(tareas_pendientes) == 0:  #mide la lista, si tiene longitud 0 imprimira lo siguiente
            print("La lista de tareas está vacía.")
        else:
            tarea_eliminada = tareas_pendientes.pop() #elimina la ultima tarea de la lista e imprimra lo siguiente
            print(f"Tarea '{tarea_eliminada}' eliminada del final de la lista.")

    #para mostrar las tareas de nuestra lista en orden inverso
    elif opcion.upper() == "3":
        if len(tareas_pendientes) == 0: #ide la lista, si tiene longitud 0 imprimira lo siguiente
            print("La lista de tareas está vacía.")
        else:
            print("Lista de tareas (en orden inverso al que se agregaron):")
            for tarea in reversed(tareas_pendientes): #usa el metodo reversed para invertir el orden de las tareas de nuestra lista
                print(tarea)

    # cuenta la cantidad de tareas
    elif opcion.upper() == "4":
        cantidad_tareas = len(tareas_pendientes) #mide la longitud de la lista e imprime la cantidad de tareas que hay
        print(f"Hay {cantidad_tareas} tareas en la lista.")

    # sale del programa
    elif opcion.upper() == "5":
        print("Fin...")
        break # cierra el bucle 

    else:
        print("Opción inválida. Por favor intenta de nuevo.") #si se ingresa un opcion erronea te vuelve a mostrar la lista de opciones