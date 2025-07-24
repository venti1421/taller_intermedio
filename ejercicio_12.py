# Validación de contraseña
# Implementa un programa que solicite una contraseña correcta (puedes fijarla en tu código)
# y permita hasta 3 intentos.

# Si el usuario acierta: imprime “¡Acceso concedido!” y termina.

# Si agota los 3 intentos: imprime “Usuario bloqueado” y termina.

correcta = "venti1421"
intento = 0
intentos = 3

while intento < intentos:
    contraseña = input("Ingresa la contraseña: ")

    if contraseña == correcta:
        print("¡Acceso concedido!")
        break
    else:
        intento += 1
if intento == intentos:
    print("Usuario bloqueado")