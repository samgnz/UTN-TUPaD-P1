"""
Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.
"""

def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia_recursiva(base, exponente - 1)


print(potencia_recursiva(10,2))