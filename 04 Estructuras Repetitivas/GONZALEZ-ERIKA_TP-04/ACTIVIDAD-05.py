"""
Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""

import random

numero_aleatorio = random.randint(0,9)
intentos = 0

while True:
            intento = input("Ingrese un numero: ")
            numero_usuario = int(intento)
            
            intentos += 1

            if numero_usuario == numero_aleatorio:
                break
            elif numero_usuario < numero_aleatorio:
                print("El número es mayor.")
            else:
                print("El número es menor.")

print(f"¡Adivinaste, era el numero {numero_aleatorio}!")

if intentos == 1:
        print("Lo adivinaste en el primer intento!")
else:
        print(f"Número de intentos necesarios: {intentos}")
