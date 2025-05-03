"""
Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

numero = int(input("Ingrese un numero: "))

invertido = 0
while numero > 0:
    ultimo_digito = numero % 10
    invertido = invertido * 10 + ultimo_digito
    numero = numero // 10
print(f"{numero} invertido es {invertido}")
