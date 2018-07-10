'''
El algoritmo fue diseñado en 1930 por el 
matemático Vojtech Jarnik y luego de manera independiente por el 
científico computacional Robert C. Prim en 1957 y redescubierto por 
Dijkstra en 1959. Por esta razón, el algoritmo es también conocido como 
algoritmo DJP por las iniciales de los participantes, o tambien conocido como algoritmo de Jarnik.
'''
import random
from pqdict import PQDict


def djp(grafo, n):
    #Se determina el nodo inicial de forma aleatoria, mediante un random en entre el numero
    #nodos
    inicio = random.randint(0, n - 1)
    print("Nodo inicial: ", inicio)
    visitado = set()
    camino_mst = []
    #Se genera una cola de prioridad para generar el orden optimizado de los resultados de los
    #caminos
    cola_prioridad = PQDict()
    actual = inicio
    return recorre_djp(camino_mst, grafo, actual, cola_prioridad, visitado)
    

def recorre_djp(camino_mst, grafo, actual, cola_prioridad, visitado):
    while (len(camino_mst) < (len(grafo) - 1)):
        for nodo in grafo.neighbors(actual):
            if nodo not in visitado and actual not in visitado:
                #Se comparan los pesos actuales, es decir en el que se encuentra parado con el
                #valor del siguiente vecino, de esta forma se actualiza el mejor valor de los pesos
                #almacenadolos en una cola de prioridad.
                if (actual, nodo) not in cola_prioridad and (nodo, actual) not in cola_prioridad:
                    peso = grafo[actual][nodo]['weight']
                    #Visualizar el peso guardado por iteración
                    #print(peso)
                    cola_prioridad.additem((actual, nodo), peso)
        visitado.add(actual)
        actual_sgte, peso = cola_prioridad.popitem()
        while (actual_sgte[1] in visitado):
            actual_sgte, peso = cola_prioridad.popitem()
        camino_mst.append(actual_sgte)
        actual = actual_sgte[1]
    return camino_mst
