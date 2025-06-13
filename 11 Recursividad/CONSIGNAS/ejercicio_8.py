"""
Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4
"""

def contar_digito(numero, digito):
    # Caso base: si el número es menor que 10, es un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    
    ultimo_digito = numero % 10  # Obtiene el último dígito
    numero_sin_ultimo = numero // 10  # Elimina el último dígito
    
    coincidencia_actual = 1 if ultimo_digito == digito else 0
    
    return coincidencia_actual + contar_digito(numero_sin_ultimo, digito)

print("Contador de dígitos en números")
print("=" * 30)
numero = int(input("Ingresa un número entero positivo: "))
digito = int(input("Ingresa el dígito a buscar (0-9): "))
resultado = contar_digito(numero, digito)
print(f"\nResultado:")
print(f"El dígito {digito} aparece {resultado} veces en {numero}")