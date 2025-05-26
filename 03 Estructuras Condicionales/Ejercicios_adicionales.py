"""
1. Validacion de contraseña
"""

contrasena_correcta = "programacion1"
contrasena_usuario = input("Introduce la contraseña: ")

if contrasena_usuario == contrasena_correcta:
    print("Contraseña correcta. Bienvenido.")
else:
    print("Contraseña incorrecta. Intenta de nuevo.")

"""
Si la contraseña ingresada es igual a la contraseña correcta se imprime Contraseña correcta
En el caso de que no sean iguales se imprime contraseña incorrecta
"""

"""
Ejemplo para que sea un bucle hasta ingresar la correcta

contrasena_correcta = "programacion1"
contrasena_correcta_ingresada = False

while not contrasena_correcta_ingresada:
    contrasena_usuario = input("Introduce la contraseña: ")
    if contrasena_usuario == contrasena_correcta:
        print("Contraseña correcta. Bienvenido.")
        contrasena_correcta_ingresada = True
    else:
        print("Contraseña incorrecta. Intenta de nuevo.")

"""








"""
2. Identificador de vocales
"""
letra = input("Ingrese una letra: ")
letra_minuscula = letra.lower()

if letra_minuscula in ["a", "e", "i", "o", "u"]:
    print("La letra es una vocal")
else:
    print("La letra no es una vocal")







"""
3. Clasificador de números
"""
numero = int(input("Ingrese un numero: "))

if numero % 2 == 0:
    print("El numero es positivo")
else:
    print("El numero es negativo")








"""
4. Comparador de números
"""
primer_numero = int(input("Ingrese un numero: "))
segundo_numero = int(input("Ingrese otro numero: "))

if primer_numero > segundo_numero:
    print("El primer numero ingresado es mayor")
else:
    print("El segundo numero ingresado es menor")





"""
5. Clima según temperatura
"""
temperatura = float(input("Ingrese la temperatura actual: "))

if temperatura <= 10:
    print("Hace frio")
elif temperatura > 10 and temperatura < 25:
    print("Está templado")
else:
    print("Hace calor")





"""
6. Detector de años bisiestos
"""
anio = int(input("Ingrese un año: "))

if anio % 4 == 0 and anio % 100 != 0:
    print("Se ingresó un año bisiesto")
elif anio % 400 == 0:
    print("Se ingresó un año bisiesto")
else:
    print("Se ingreso un año no bisiesto")





"""
7. Ajustador de frases
"""
frase = input("Ingrese una frase o palabra: ")

if not frase.endswith('.'):
    frase += '.'

print(frase)








"""
8. Validador de contraseña segura y 9. Mejorando mensajes de error
"""
contrasena = input("Ingrese una contraseña: ")

if len(contrasena) < 8:
    print("La contraseña no es segura. Debe tener al menos 8 caracteres")
elif len(contrasena) > 20:
    print("La contraseña no es segura. No más de 20 caracteres")
elif not any(caracter.isupper() for caracter in contrasena):
    print("La contraseña no es segura. Ingrese al menos una mayuscula")
elif not any(caracter.isdigit() for caracter in contrasena):
    print("La contraseña no es segura. Ingrese al menos un numero")
else:
    print("Contraseña ingresada")







"""
10. Piedra, papel o tijera
"""
jugador_1 = input("Ingresa PIEDRA/PAPEL/TIJERA para el jugador 1:")
jugador_2 = input("Ingresa PIEDRA/PAPEL/TIJERA para el jugador 2:")

jugador_1_minuscula = jugador_1.lower()
jugador_2_minuscula = jugador_2.lower()


if jugador_1_minuscula == jugador_2_minuscula:
    print("Empate")
elif jugador_1_minuscula == 'piedra' and jugador_2_minuscula == 'tijera':
    print ("Ganó el jugador 1.")
elif jugador_1_minuscula == 'papel' and jugador_2_minuscula == 'piedra':
    print ("Ganó el jugador 1.")
elif jugador_1_minuscula == 'tijera' and jugador_2_minuscula == 'papel':
    print ("Ganó el jugador 1.")
else:
    print ("Ganó el jugador 2.")