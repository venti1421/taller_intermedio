# Búsqueda con while-else
# Dada la lista [4, 8, 15, 16, 23, 42], pide al usuario un número a buscar.

# Recorre la lista con un while y, si lo encuentras, muestra su índice y haz break.

# Si terminas el bucle sin encontrarlo, el bloque else debe imprimir “Número no encontrado”.

lista = [4, 8, 15, 16, 23, 42]
numero = int(input("Ingrese un numero a buscar: "))

i = 0
while i < 6:  
    if lista[i] == numero:
        print(f"Numero encontrado en el indice: {i}")
        break
    i += 1
else:
    print("Numero no encontrado")