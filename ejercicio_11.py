# Suma hasta cero
# Crea un programa que lea números del usuario repetidamente con while hasta que ingrese un 0. Al finalizar,
# muestra la suma de todos los valores ingresados (excluyendo el cero).


suma = 0
numero = int(input("Esto suma numeros hasta que digites 0: "))

while numero != 0:
    suma += numero
    numero = int(input("Esto suma numeros hasta que digites 0: "))
print(f"La suma total fue: {suma}")