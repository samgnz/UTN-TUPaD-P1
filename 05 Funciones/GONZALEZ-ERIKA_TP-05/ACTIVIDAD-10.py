"""
Crear una función llamada calcular_promedio(a, b, c) que reciba
tres números como parámetros y devuelva el promedio de ellos.
Solicitar los números al usuario y mostrar el resultado usando esta
función.
"""

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

def main():
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    promedio = calcular_promedio(num1, num2, num3)
    print("El promedio de los tres números es: ", promedio)

main()




