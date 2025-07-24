# Uso de break y continue
# Escribe un programa con while True que recorra números de 1 en adelante y:

# Use continue para saltar e imprimir solo los números que no sean múltiplos de 3.

# Detenga el bucle (break) cuando alcance el número 20.

n = 1
while True:
    if n % 3 == 0:
        n += 1
        continue  
    print(n)
    if n == 20:
        break  
    n += 1