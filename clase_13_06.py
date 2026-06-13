def mostrar_menu():
    print("---M E N Ú---")
    print("[1] °C -> °F")
    print("[2] °F -> °C")
    print("[3] Salir")
mostrar_menu()

def pedir_temperatura():
    temp = float(input("Ingrese una temperatura: \n"))
    return temp
pedir_temperatura()

def motrar_resultado(orig, conv, ud):
    print(orig)
    print(conv)
    print(ud)
motrar_resultado(3.0, 40, "CF")

c = float(input("Ingrese los grados: \n"))
def cel_a_fa(c):
    return (c* 9/5) +32
print(cel_a_fa(c))

f = float(input("ingrese los grados:\n"))
def fa_a_cel(f):
    return(f - 32) * 5/9
print(fa_a_cel(f))
