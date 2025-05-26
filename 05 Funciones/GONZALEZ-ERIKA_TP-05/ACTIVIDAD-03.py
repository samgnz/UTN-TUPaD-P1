"""
Crear una función llamada informacion_personal(nombre, apellido,
edad, residencia) que reciba cuatro parámetros e imprima: “Soy
[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
los datos al usuario y llamar a esta función con los valores ingresados.
"""

def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

def main():
    nombre = input("Ingrese su nombre")
    apellido = input("Ingrese su nombre")
    edad = input("Ingrese su nombre")
    residencia = input("Ingrese su nombre")
    reporte = informacion_personal(nombre, apellido, edad, residencia)
    print(reporte)


#Programa Principal
main()