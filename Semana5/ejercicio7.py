"""
Ejercicio 7:
Una persona registra cuánto dinero ahorra cada mes en una lista.
Cada valor representa el ahorro mensual.

Se requiere calcular el ahorro total acumulado.

Debe implementar:
1. Una solución con iteración
2. Una solución con recursividad
"""

def ahorro_total_ciclo(ahorros):
    """
    Retorna el ahorro total usando iteración.
    """
    acumulado = 0 
    for ahorro in ahorros:
        acumulado = acumulado + ahorro
    return acumulado


def ahorro_total_recursivo(ahorros):
    """
    Retorna el ahorro total usando recursividad.
    """
    if len(ahorros) == 0:
        return 0
    else:
        return ahorros[0] + ahorro_total_recursivo(ahorros[1:])
    
ahorros = [1200, 5000, 10000, 2500]
print(ahorro_total_recursivo(ahorros))
print(ahorro_total_ciclo(ahorros))