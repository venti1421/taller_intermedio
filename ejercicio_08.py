# Lista de cuadrados
# Genera una lista que contenga los cuadrados de los números del 1 al 10
# usando un for, y luego muestra la lista completa.

lista = []
for n in range(1, 11):
    numero = n ** 2  
    lista.append(numero)
print("Lista de cuadrados del 1 al 10:", lista)