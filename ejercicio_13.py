# Menú repetitivo
# Desarrolla un menú en bucle while con estas opciones:

# Sumar dos números

# Restar dos números

# Multiplicar dos números

# Salir
# Elige la opción, pide los operandos, muestra el resultado y vuelve a mostrar
# el menú hasta que seleccione “Salir”.

while True:
    print("\n---Menu---")
    print("1. Sumar dos numeros")
    print("2. Restar dos numeros")
    print("3. Multiplicar dos numeros")
    print("4. Salir")
    
    opcion = input("Seleccione una opcion: ")
    
    if opcion == "1":
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 + num2
        print(f"La suma es: {resultado}")
        
    elif opcion == "2":
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 - num2
        print(f"La resta es: {resultado}")
        
    elif opcion == '3':
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numero: "))
        resultado = num1 * num2
        print(f"La multiplicacion es: {resultado}")
        
    elif opcion == '4':
        break
    