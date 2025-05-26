"""
Crear una función llamada segundos_a_horas(segundos) que reciba
una cantidad de segundos como parámetro y devuelva la cantidad
de horas correspondientes. Solicitar al usuario los segundos y mostrar
el resultado usando esta función.
"""

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return horas

def main():
    segundos = int(input("Ingrese la cantidad de segundos deseada: "))
    horas = segundos_a_horas(segundos)

    print(f"{segundos} segundos son {horas} horas")

main()