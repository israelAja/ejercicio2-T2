def suma_recursiva(lista, pi,pf):
    if pi > pf:
        return 0
    else:
        return lista[pi-1] + suma_recursiva(lista, pi + 1, pf)
    n= int (input("Ingrese cantidad de elemnetos: "))
lista = []

def suma_recursiva(lista, pi, pf):

    if pi > pf:
        return 0
    return lista[pi - 1] + suma_recursiva(lista, pi + 1, pf)

n = int(input("Ingrese cantidad de elementos: "))
lista = []
for i in range(n):
    numero = int(input("Ingrese número: "))
    lista.append(numero)
pi = int(input("Ingrese posición inicial: "))
pf = int(input("Ingrese posición final: "))


resultado = suma_recursiva(lista, pi, pf)
print("La suma es:", resultado)