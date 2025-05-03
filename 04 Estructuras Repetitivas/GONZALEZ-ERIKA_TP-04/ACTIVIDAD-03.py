"""
Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores.
"""

valorInicial = int(input("Ingrese el primer valor: "))
valorFinal = int(input("Ingrese el segundo valor: "))
suma = 0
    
for numero in range(valorInicial + 1, valorFinal):
    suma += numero
print(f"La suma de los enteros entre {valorInicial} y {valorFinal} (sin incluirlos) es: {suma}")
