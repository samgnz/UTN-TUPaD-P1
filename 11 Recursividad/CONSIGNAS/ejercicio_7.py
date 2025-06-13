"""
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
    """

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

print("Calculadora de bloques para pirámide")
print("=" * 35)
n = int(input("Ingresa el número de bloques en la base: "))
resultado = contar_bloques(n)

print(f"\nPara una pirámide con base de {n} bloques:")
print(f"Total de bloques necesarios: {resultado}")

descomposicion = " + ".join(str(i) for i in range(n, 0, -1))
print(f"Cálculo: {descomposicion} = {resultado}")

