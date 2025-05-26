"""
Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
como parámetro y devuelva el área del círculo. calcular_perimetro_
circulo(radio) que reciba el radio como parámetro y devuelva
el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
funciones para mostrar los resultados.
"""

def calcular_area_circulo(radio):
    area = 3.14 * (radio * 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro


def main():
    radio = int(input("Ingrese el radio deseado: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"El perimetro {perimetro} y el area es {area}")


main()