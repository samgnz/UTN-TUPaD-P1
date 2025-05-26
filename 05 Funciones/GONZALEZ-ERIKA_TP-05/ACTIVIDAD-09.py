"""
Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
una temperatura en grados Celsius y devuelva su equivalente en
Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
resultado usando la función.
"""

def celsius_a_fahrenheit(celsius):
    fahrenheit = ((celsius * (9/5)) + 32)
    return fahrenheit


def main():
    celsius = float(input("Ingrese los grados en celcius: "))
    fahr = celsius_a_fahrenheit(celsius)

    print(f"{celsius}ºC son {fahr}ºF")


main()