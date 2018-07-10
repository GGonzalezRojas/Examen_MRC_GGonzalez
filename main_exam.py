import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import matriz_nodos as mn
from algoritmo_arbol_jdp import djp


def graficar(grafo, posicion, n, colors, camino_mst=0):
    etiquetas = {}
    for indice, nodo in enumerate(grafo.nodes()):
        etiquetas[nodo] = indice
    nx.draw_networkx_nodes(grafo, posicion, node_shape='8', node_color=colors, node_size=600, alpha=1)
    nx.draw_networkx_edges(grafo, posicion, width=3, alpha=0.8)
    nx.draw_networkx_labels(grafo, posicion, etiquetas, font_size=14, font_color='r')
    nx.draw_networkx_edges(grafo, pos=posicion, node_shape='8', edgelist=camino_mst, edge_color='r')
    plt.show()


def principal_v1(n):
    #Se comienza generando un conjunto de puntos aleatorios, los que representán los nodos 
    #en el escenario planteado.
    matriz_nodos =  mn.generar_matriz_distancias(n)
    grafo = nx.Graph(matriz_nodos)
    posicion = nx.spring_layout(grafo)
    colors = np.random.rand(n)
    graficar(grafo, posicion, n, colors)
    #Camino del minimo spanning tree (MST)
    camino_mst = djp(grafo, n)
    print(camino_mst)
    graficar(grafo, posicion, n, colors, camino_mst)
    
principal_v1(20)
