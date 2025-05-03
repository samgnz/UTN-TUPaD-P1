"""
Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor).
"""

cant_numeros = 100
sumatoria = 0

for contador in range(1,cant_numeros+1):
    print(f"Ingrese el número {contador}: ")
    numero = int(input())
    sumatoria += numero

print("La media es",(sumatoria/cant_numeros))