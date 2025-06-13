"""
Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial
de todos los números enteros entre 1 y el número que indique el usuario
"""

def factorial_recursivo(x):
	if x == 0:
		return 1
	else:
		return x * factorial_recursivo(x-1)

print(factorial_recursivo(5))