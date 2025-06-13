"""
Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
"""
def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    
    if numero == 1:
        return "1"
    return decimal_a_binario(numero // 2) + str(numero % 2)


print(decimal_a_binario(13))