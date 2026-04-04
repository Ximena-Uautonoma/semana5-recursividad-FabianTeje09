"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    numero = 1
    p = 0 
    while numero <= n:
        if numero % 2 == 0:
            p = p + 1
        numero = numero + 1
    return p


def contar_pares_recursivo(n):
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return 1 + contar_pares_recursivo(n - 1)
        else:
            return contar_pares_recursivo(n - 1)






n = int(input("Ingrese el valor de n: "))
print(contar_pares_ciclo(n))
print(contar_pares_recursivo(n))