"""
Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0.
"""
suma_total = 0
contador = 0


while True:
        entrada = input(f"Ingrese el número {contador + 1} (0 para terminar): ")
        numero = int(entrada)
            
        if numero == 0:
            break
                
        suma_total += numero
        contador += 1
print(f"El total acumulado es: {suma_total}")