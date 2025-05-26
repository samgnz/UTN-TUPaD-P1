"""
Crear una función llamada calcular_imc(peso, altura) que reciba el
peso en kilogramos y la altura en metros, y devuelva el índice de
masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
para mostrar el resultado con dos decimales.
"""


def calcular_imc(peso, altura):
    IMC = peso / (altura ** 2)

    return IMC


def main():
    peso = float(input("Por favor, ingrese su peso en kg: "))
    altura = float(input("Por favor, ingrese su altura en metros: "))

    IMC = calcular_imc(peso, altura)

    print("Tu IMC es:",IMC)


main()