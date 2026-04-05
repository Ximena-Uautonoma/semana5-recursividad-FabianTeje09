"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando iteración.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    lista = []  #lista vacia
    numero = 1 #indice 0 
    while numero <= n: 
        lista.append(numero) #agregar la variable a la lista
        numero = numero + 1 # se suma hasta ser mayor a n
    return lista #retorna la lista


def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    # Escriba aquí su solución y borre la palabra pass de acontinuación
    if n == 1: # si n = 1 retorna [1]
        return [n]
    else:
        return contar_recursivo( n - 1) + [n] 

n = int(input("Ingrese el valor de n: "))
print(contar_ciclo(n))
print(contar_recursivo(n))
