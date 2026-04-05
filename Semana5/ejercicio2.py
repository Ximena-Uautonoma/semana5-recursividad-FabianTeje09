"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(num):
    """
    Retorna la suma de los primeros n números usando un ciclo.
    """
    numero = 1 
    suma_numeros = 0
    while numero <= num:
        numero = numero + 1
        suma_numeros = suma_numeros + numero
    return suma_numeros




def suma_recursiva(n):
    """
    Retorna la suma de los primeros n números usando recursividad.
    """
    if n == 1:
        return 1
    else:
        return n + suma_recursiva(n -1)    

# def suma_ciclo
num = int(input("Ingrese un numero entero positivo: "))
print(suma_ciclo(num))

#def suma recursiva
n = int(input("ingrese valor de N: "))
print(suma_recursiva(num))
