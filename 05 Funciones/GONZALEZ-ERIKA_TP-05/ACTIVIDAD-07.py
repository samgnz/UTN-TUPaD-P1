"""
Crear una función llamada operaciones_basicas(a, b) que reciba
dos números como parámetros y devuelva una tupla con el resultado
de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
de forma clara.
"""

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

def main():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    
    resultados = operaciones_basicas(num1, num2)
    
    print("Resultados:")
    print(f"Suma: {resultados[0]}")
    print(f"Resta: {resultados[1]}")
    print(f"Multiplicación: {resultados[2]}")
    print(f"División: {resultados[3]}")

main()