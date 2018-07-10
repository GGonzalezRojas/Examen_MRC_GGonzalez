import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import distance


def crear_coordenadas_random(n):
    #Funcion genera puntos aleatorios mediante una dristribución normal mendiante numpy random standard normal
    coordenadas = [np.random.standard_normal(n), np.random.standard_normal(n)]
    plt.plot(coordenadas[0], coordenadas[1], 'ro')
    plt.show()
    return coordenadas


def obtener_dist(array_x, array_y, n):
    dist = []
    for actual in range(n):
        punto_1 = [array_x[actual], array_y[actual]]
        for siguiente in range(n):
            punto_2 = [array_x[siguiente], array_y[siguiente]]
            dist.append(distance.euclidean(punto_1, punto_2))
    return generar_matriz(max(dist), n, array_x, array_y)


def vecinos(ajuste, matriz, n, arr_x, arr_y, punto_1, i, marca):
    for j in range(n):
        punto_2 = [arr_x[j], arr_y[j]]
        dist = distance.euclidean(punto_1, punto_2)
        if dist <= ajuste and matriz[i][j] == 0 and i != j:
            matriz[i][j] = dist
            marca = False
    return matriz, marca


def generar_matriz(max, n, arr_x, arr_y):
    #Se genera una matriz de ceros la cual almacenará los pesos de las distancias.
    matriz = np.zeros((n, n), dtype=float)
    ajuste_1, ajuste_2, ajuste_3, ajuste_4 = 1/4 * max, 2/4 * max, 3/4 * max, max
    for i in range(n):
        punto_1 = [arr_x[i], arr_y[i]]
        marca = True
        if marca is True:
            matriz, marca = vecinos(ajuste_1, matriz, n, arr_x, arr_y, punto_1, i, marca)
        if marca is True:
            matriz, marca = vecinos(ajuste_2, matriz, n, arr_x, arr_y, punto_1, i, marca)
        if marca is True:
            matriz, marca = vecinos(ajuste_3, matriz, n, arr_x, arr_y, punto_1, i, marca)
        if marca is True:
            matriz, marca = vecinos(ajuste_4, matriz, n, arr_x, arr_y, punto_1, i, marca)
    return matriz


def generar_matriz_distancias(n):
    #Se generan puntos aleatorios mediante la funcion creada 'crear_coordenadas_random'
    array_coord_x, array_coord_y = crear_coordenadas_random(n)
    #Se determina la distancia euclidiana entre ls puntos antes creados, de estos se obtiene
    #el maximo el cual marcará el punto de referencia para la asiganción de las medidas del árbol
    matriz =  obtener_dist(array_coord_x, array_coord_y, n)
    #print(matriz)
    return matriz




