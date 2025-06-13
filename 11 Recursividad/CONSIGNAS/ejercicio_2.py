"""
Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.
"""

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion-1) + fibonacci(posicion-2)
    
    

for i in range(10):
    print(f"En la posicion {i}, el numero de fibonacci es {fibonacci(i)}")