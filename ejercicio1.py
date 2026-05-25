import random


def buscar_multiplos(arreglo, indice, minimo, maximo):

    # Caso base
    if indice == len(arreglo):
        return minimo, maximo

    numero = arreglo[indice]

    # Verificar múltiplos de 3
    if numero % 3 == 0:

        if minimo is None or numero < minimo:
            minimo = numero

        if maximo is None or numero > maximo:
            maximo = numero

    # Llamada recursiva
    return buscar_multiplos(arreglo, indice + 1, minimo, maximo)



n = int(input("Ingrese el tamaño del arreglo: "))

# Crear arreglo
arreglo = []


for i in range(n):
    numero = random.randint(10, 9999)
    arreglo.append(numero)


print("Arreglo generado:")
print(arreglo)

# Buscar mínimo y máximo múltiplos de 3
minimo, maximo = buscar_multiplos(arreglo, 0, None, None)


if minimo is not None and maximo is not None:

    promedio = (minimo + maximo) / 2

    print("Mínimo múltiplo de 3:", minimo)
    print("Máximo múltiplo de 3:", maximo)
    print("Promedio:", promedio)

else:
    print("No existen múltiplos de 3")