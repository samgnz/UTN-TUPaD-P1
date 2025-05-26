"""
Calcular área y perimetro de un rectangulo
"""
ancho = int(input("Ingrese la ancho del rectangulo: "))
alto = int(input("Ingrese la alto del rectangulo: "))

area = ancho * alto
perimetro = (ancho * 2) + (alto * 2)

print("El area del rectangulo es: ", area)
print("El area del perimetro es: ", perimetro)




"""
Realizar la conversión de temperatura de Celsius a Fahrenheit
"""
celcius = int(input("Ingrese los grados en celcius: "))

fahrenheit = ((celcius * (9/5)) + 32)

print(celcius, " en fahrenheit son ", fahrenheit)





"""
Uso de booleanos
"""
a = True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
print("not b:", not b)




"""
Prueba de escritorio
"""
a = 5
b = 3
c = a + b
a = 2
print(c)  
# el cambio del valor de a no modifica a c porque se calcula con su valor anterior, si se imprime el valor de a al final del programa este si cambia su valor
# ya que las variables son mutables




"""
Diagrama de flujo – Cuadrado de un número
"""
numero = int(input("Ingrese un número: "))

cuadrado = numero ** 2

print("El cuadrado de", numero, "es", cuadrado)





""""
Intercambio de variables
"""
x = 10
y = 20

print("El valor de x es:", x, "y el valor de y es:", y)

x = x + y
y = x - y
x = x - y

print("El nuevo valor de x es:", x, "y el nuevo valor de y es:", y)




"""
Cálculo del IMC
"""
peso = float(input("Por favor, ingrese su peso en kg: "))
altura = float(input("Por favor, ingrese su altura en metros: "))

IMC = peso / (altura ** 2)

print("Tu IMC es:",IMC)





"""
Contador de caracteres en un nombre
"""
nombre = input("Por favor, ingrese su nombre completo: ")


nombre_sin_espacios = nombre.replace(" ", "")
total_letras = len(nombre_sin_espacios)

primeras_tres_letras = nombre[:3]

mayusculas_alternadas = "".join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(nombre))

print("Cantidad de letras (sin espacios):", total_letras)
print("Primeras 3 letras:", primeras_tres_letras)
print("Nombre con mayúsculas y minúsculas alternadas:", mayusculas_alternadas)




"""
Operaciones con números flotantes
"""
a = 7.5
b = 3.2

suma = a + b
print(suma)

redondeo = round(a/b,2) #el primer parametro es el numero, el segundo es la cantidad de digitos
print(redondeo)

potencia = a ** b
print(potencia)






"""
Descuento sobre precio original
"""
precio_original = float(input("Ingrese el precio de un producto: "))
porcentaje = float(input("Ingrese el porcentaje de descuento: "))

precio_final = precio_original * (1-(porcentaje / 100))

print("Este es el precio final:", precio_final)