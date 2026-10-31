class Nodo:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None

class ListEnlazada:
    def __init__(self):
        self.cabeza = None
        
    def Insertar_Nodo_al_Inicio(self, numero):
        nuevo_nodo = Nodo(numero)
        nuevo_nodo.siguiente = self.cabeza 
        self.cabeza = nuevo_nodo
        
    def Insertar_Nodo_al_Final(self, numero):
        nuevo_nodo = Nodo(numero)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo

    def Eliminar_Nodo_al_Inicio(self):
        if self.cabeza is None:
            return 
        
     
        self.cabeza = self.cabeza.siguiente

    def Eliminar_Nodo_al_Final(self):
        if self.cabeza is None:
            return  
        
       
        if self.cabeza.siguiente is None:
            self.cabeza = None
            return
        
       
        actual = self.cabeza
        while actual.siguiente.siguiente:
            actual = actual.siguiente
        
        # Desvincular el último nodo
        actual.siguiente = None

    def imprimir_lista_enlazada(self):
        actual = self.cabeza
        while actual:
            print(actual.numero , "-> " , end="")
            actual = actual.siguiente
        print("None") 


Mi_lista = ListEnlazada()
Mi_lista.Insertar_Nodo_al_Inicio(2)
Mi_lista.Insertar_Nodo_al_Inicio(1)
Mi_lista.Insertar_Nodo_al_Final(4)
Mi_lista.Insertar_Nodo_al_Final(5)

print("Lista original:")
Mi_lista.imprimir_lista_enlazada()

print("\nDespués de eliminar al inicio:")
Mi_lista.Eliminar_Nodo_al_Inicio()
Mi_lista.imprimir_lista_enlazada()

print("\nDespués de eliminar al final:")
Mi_lista.Eliminar_Nodo_al_Final()
Mi_lista.imprimir_lista_enlazada()