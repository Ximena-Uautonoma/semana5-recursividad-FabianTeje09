"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    acumulado = 1 # acumulacion de base
    i = 0  #contador 
    while i < exponente:
        acumulado = acumulado * base
        i = i + 1 #avance de contado
    return acumulado 

        
    


def potencia_recursiva(base, exponente):
    if exponente == 0: #si el exponente es = 0 retorna 1 
        return 1 
    else:
        return base * potencia_recursiva( base, exponente - 1) 
    
base = int(input("Ingrese valor de la base: "))
exponente = int(input("Ingrese valor del exponente: "))
print(potencia_ciclo(base, exponente))
print(potencia_recursiva(base, exponente))

