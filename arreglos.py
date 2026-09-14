#Declarando un arreglo
numeros = [10,20,30,40,50]

#Imprimimos un elemento espe. del arreglo
print(numeros[2])

#Reasignación
numeros[3] = 35
print(numeros)

#Agrega un nuevo valor al final del arreglo
numeros.append(60)
print(numeros)

#Eliminamos un valor en el arreglo
numeros.remove(35)
print(numeros)

#Eliminamos un valor del arreglo usando la posición
numeros.pop(4)
print(numeros)

frutas = ["Manzana", "Fresa", "Sandia", "Mango", "Melon", "Platano"]
frutas.pop(4)
print(frutas)


frutas.remove("Manzana")
print(frutas)