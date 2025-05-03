"""
Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario.
"""

suma = 0
numero = int(input("Ingrese un numero: "))

for i in range(numero + 1):  # range(n+1) genera números desde 0 hasta n inclusive
    suma += i
print(f"La suma de todos los números desde 0 hasta {numero} es: {suma}")