"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    acumulado = 1 #acumulacion de num para el factorial
    numero = 1 #contador de num
    while numero <= n:
        acumulado = acumulado * numero
        numero = numero + 1 #avance del contador
    return acumulado 


def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return factorial_recursivo(n - 1) * n


n = int(input("Ingrese valor de n: "))
print(factorial_ciclo(n))
print(factorial_recursivo(n))