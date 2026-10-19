def pilas():
    while True:
        pila = []
        print("\n--- Inicio del Programa de Pilas ---")
        
        while True:
            print("\nMenú:")
            print("1. Insertar pila")
            print("2. Borrar en pila")
            print("3. Listar pila")
            print("4. Salir")
            
            opcion = input("Selecciona una opción: ")
            
            if opcion == '1':
                numero = input("Ingresa un número a la pila: ")
                pila.append(numero)
                print(f"Número {numero} agregado a la pila.")
                
            elif opcion == '2':
                if len(pila) > 0:
                    borrado = pila.pop() 
                    print(f"Se sacó el número {borrado} de la pila.")
                else:
                    print("La pila está vacía, no hay elementos para borrar.")
                    
            elif opcion == '3':
                print(f"Contenido actual de la pila: {pila}")
                
            elif opcion == '4':
                print("Saliendo del menú de pilas...")
                break
                
            else:
                print("Opción no válida. Intenta de nuevo.")
                
      
        repetir = input("\n¿Desea ejecutar nuevamente el programa? (s/n): ")
        if repetir.lower() != 's':
            print("Fin del programa.")
            break
pilas()