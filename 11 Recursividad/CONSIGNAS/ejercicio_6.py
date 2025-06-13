"""
Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
"""
def suma_digitos(num):
    if num < 10:
        return num
    
    ultimo_digito = num % 10  # Obtiene el último dígito
    numero_sin_ultimo = num // 10  # Elimina el último dígito
    
    return ultimo_digito + suma_digitos(numero_sin_ultimo)

numero = int(input("Ingrese un numero: "))
resultado = suma_digitos(numero)
print(f"La suma de los digitos {numero} es {resultado}")

