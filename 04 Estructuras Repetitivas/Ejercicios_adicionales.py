"""
1. Bucle for para números pares
"""

# con rango dos en dos
for numero in range(2, 21, 2):
    print(numero)

# con if si es par
for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)




"""
2. Bucle while con suma acumulativa
"""
suma = 0

print("Ingresa números para sumarlos hasta llegar a 100")

while suma <= 100:
    numero = float(input("Ingresa un número: "))
    suma += numero 
    print(f"Suma actual: {suma}")

print(f"La suma ha superado 100!")
print(f"La suma total es: {suma}")




"""
3. Filtrar palabras por letra inicial
"""
palabras = ["apple", "banana", "avocado", "pear", "apricot", "blueberry", "almond", "orange"]

print("Lista original de palabras:")
print(palabras)

print("Palabras que comienzan con 'a':")
for palabra in palabras:
    if palabra.startswith('a'):
        print(palabra)


"""
# Método 2: Usando comprensión de listas
print("\nUsando comprensión de listas:")
palabras_con_a = [palabra for palabra in palabras if palabra.startswith('a')]
print(palabras_con_a)

# Método 3: Usando la función filter
print("\nUsando función filter:")
palabras_filtradas = list(filter(lambda palabra: palabra.startswith('a'), palabras))
print(palabras_filtradas)
"""





"""
4. Tablas de multiplicar del 7
"""
print("Tabla de multiplicar del 7:")
print("--------------------------")

for i in range(1, 11):
    resultado = 7 * i
    print(f"7 x {i} = {resultado}")







"""
5. Contador de vocales
"""
texto = input("Por favor, ingresa un texto: ")
texto = texto.lower()

contador_total = 0

contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0


for caracter in texto:
    if caracter in "aeiou":
        contador_total += 1
        
        if caracter in "a":
            contador_a += 1
        elif caracter in "e":
            contador_e += 1
        elif caracter in "i":
            contador_i += 1
        elif caracter in "o":
            contador_o += 1
        elif caracter in "u":
            contador_u += 1

print(f"Resultados:")
print(f"El texto contiene {contador_total} vocales en total.")
print(f"- a: {contador_a}")
print(f"- e: {contador_e}")
print(f"- i: {contador_i}")
print(f"- o: {contador_o}")
print(f"- u: {contador_u}")







"""
6. Números repetidos en una lista
"""
numeros = [3,1,3,5,1]

print("Lista original:", numeros)

repetidos = []

for num in numeros:
    if numeros.count(num) > 1 and num not in repetidos:
        repetidos.append(num)

print("Números que aparecen más de una vez:")
print(repetidos)




"""
7. FizzBuzz
"""
for numero in range(1, 101):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)






"""
8.Frecuencia de palabras
"""
texto = "hola hola mundo"
palabras = texto.split()

frecuencia = {}

for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1

print("Frecuencia:", frecuencia)




"""
9. Filtrar consonantes
"""
texto = input("Ingrese una cadena de texto: ")
vocales = "aeiou"
resultado = ""

for letra in texto:
    if letra not in vocales:
        resultado += letra

print("Consonantes:", resultado)





"""
10. Números primos
"""
numero = int(input("Ingresa un número entero positivo: "))

print("Números primos hasta", numero, ":")

for num in range(2, numero + 1): 
    es_primo = True
    for i in range(2, int(num**0.5) + 1): 
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)
