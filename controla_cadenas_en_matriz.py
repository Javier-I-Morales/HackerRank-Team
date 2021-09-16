import numpy as np
import re

a=['a','a','a','a']

a = ','.join(a)


def verifica_horizontal(array):
    return verificar(array)


def verifica_vertical(array):
    arrayt = np.transpose(array)
    return verificar(arrayt)


def verificar_diagonales(array):
    arrayd = crea_diagonales(array)
    return verificar(arrayd)


def crea_diagonales(array):
    lista = []
    indice = 0
    while indice < 3:
        lista.append(np.diag(array, indice))
        indice += 1
    indice = -2
    while indice < 0:
        lista.append(np.diag(array, indice))
        indice += 1
    arrayR = np.flip(array,1)
    print("")
    while indice < 3:
        lista.append(np.diag(arrayR, indice))
        indice += 1
    indice = -2
    while indice < 0:
        lista.append(np.diag(arrayR, indice))
        indice += 1
    return lista


def verificar(array):
    resultado = False
    for arreglo in array:
        arreglo = ','.join(arreglo)
        if re.findall(a, arreglo):
            resultado = True
    return resultado


m = np.array([['a','f','a','d','t','d'],['a','b','a','a','r','a'],['a','b','d','a','b','f'],['d','b','a','d','t','f'],['a','a','a','d','t','t'],['a','f','d','d','t','f']])

print(m)
print("")
print(np.flip(m,1))

def control_mutantes(m):
    resultado = False
    if verifica_horizontal(m) or verifica_vertical(m) or verificar_diagonales(m):
        resultado = True
    print(resultado)
    return resultado

control_mutantes(m)
