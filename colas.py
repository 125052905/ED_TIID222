def colas():
    while True:
        cola = []
        print("\n--- Inicio del Programa de Colas ---")
        
        while True:
            print("\nMenú:")
            print("1. Insertar cola")
            print("2. Borrar en cola")
            print("3. Listar cola")
            print("4. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == '1':
                numero = input("Ingresa un número a la cola: ")
                cola.append(numero)
                print(f"Número {numero} agregado a la cola.")
                
            elif opcion == '2':
                if len(cola) > 0:
                    borrado = cola.pop(0)
                    print(f"Se sacó el número {borrado} de la cola.")
                else:
                    print("La cola está vacía, no hay elementos para borrar.")
                    
            elif opcion == '3':
                print(f"Contenido actual de la cola: {cola}")
                
            elif opcion == '4':
                print("Saliendo del menú de colas...")
                break
                
            else:
                print("Opción no válida. Intenta de nuevo.")
                
        repetir = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ")
        if repetir.lower() != 's':
            print("Fin del programa.")
            break
colas()