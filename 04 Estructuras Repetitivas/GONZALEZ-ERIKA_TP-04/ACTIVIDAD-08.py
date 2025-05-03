"""
Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""

pares = 0
impares = 0
positivos = 0
negativos = 0

for num in range(100):
        numero = int(input(f"Ingrese el número {num+1}: "))
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
            
        if numero > 0:
            positivos += 1
        else:
            negativos += 1
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")            