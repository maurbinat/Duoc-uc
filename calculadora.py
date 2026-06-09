print("-----Calculadora-------")
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese el otro numero: "))
num3 = int(input("Ingrese el otro numero: "))
while True:
    print("Menú de opcion")
    print("1.- Sumar")
    print("2.- Restar")
    print("3.- Dividir")
    print("4.- Multiplicar")
    opc = int(input("Ingrese una opcion: "))
    if opc == 1:
        print("La suma es: " , num1 + num2 + num3)
        break
    if opc == 2:
        print("La resta es: " , num1 - num2 - num3)
        break
    if opc == 3:
        print("La division es: " , num1 / num2 / num3)
        break
    if opc == 4:
        print("La multiplicacion es: " , num1 * num2 * num3)
        break
