"""
Pasando una lista de numeros, obtener la suma total de los mismos de forma recursiva"""


def sum_list(list):
    if len(list)==0:
        return 0
    else:
        return list[0]+sum_list(list[1:])
    
lista_nums = [1,2,3,4,5]

#print(f"el valor total de la lista es {sum_list(lista_nums)}")


"""
Realizar una funcion recursiva que reciba un numero y una frase y la repita el numero de veces ingresado
"""

def repetir_frase(num_a_repetir, frase):
    if num_a_repetir>= 1:
        print(frase)
        repetir_frase(num_a_repetir-1, frase)

#repetir_frase(3, "Hola mundo")


"""
Realizar la suma de los primeros n valores positivos de forma recursiva
"""
def suma_recursiva(num):
    if num == 0:
        return 0
    else:
        return num + suma_recursiva(num-1)
    
#print(suma_recursiva(10))


"""
Realizar una funcion recursiva que permita sumas los n valores primos
"""
def es_primo(num):
    if num <=1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def suma_n_primos(numero):
    if numero == 1:
        return 0
    elif es_primo(numero):
        return numero+suma_n_primos(numero-1)
    else:
        return suma_n_primos(numero-1)

#print(suma_n_primos(8))

"""
Laberito - tenemos la matriz laberinto y hay que crear un camino de 0 para salir
"""

def resolver_laberinto (laberinto, x, y, camino):
    if x < 0 or y <0 or x >= len(laberinto) or y >= len(laberinto[0]) or laberinto[x][y] == 1:
        return False
    camino.append((x, y))

    if x == len(laberinto) - 1 and y == len(laberinto[0]) - 1:
        return True
    laberinto[x][y] = 1

    if (resolver_laberinto(laberinto, x + 1, y, camino) or #abajo
        resolver_laberinto(laberinto, x, y + 1, camino) or #derecha
        resolver_laberinto(laberinto, x - 1, y, camino) or #arriba
        resolver_laberinto(laberinto, x, y - 1, camino)): #izquierda
        return True
    
    camino.pop()
    laberinto[x][y] = 0
    return False


laberinto = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0]
]

camino = []

resolver_laberinto(laberinto,0,0, camino)
print(camino)