import matplotlib.pyplot as plt
import networkx as nx
import heapq

def dijkstra_visual(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    visitados = set()
    cola = [(0, inicio)]

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))

    return distancias

def mostrar_grafo(grafo, distancias=None):
    G = nx.DiGraph()
    for nodo in grafo:
        for vecino, peso in grafo[nodo].items():
            G.add_edge(nodo, vecino, weight=peso)

    pos = nx.spring_layout(G)
    pesos = nx.get_edge_attributes(G, 'weight')
    
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos)
    
    if distancias:
        etiquetas = {nodo: f"{nodo}\n{distancias[nodo]}" for nodo in G.nodes}
        nx.draw_networkx_labels(G, pos, labels=etiquetas)

    plt.title("Grafo y distancias desde nodo inicial")
    plt.show()

# Mismo grafo de antes
grafo = {
    'A': {'B': 5, 'C': 1},
    'B': {'C': 2, 'D': 1},
    'C': {'D': 4, 'E': 8},
    'D': {'E': 3, 'F': 6},
    'E': {},
    'F': {}
}

inicio = 'A'
distancias = dijkstra_visual(grafo, inicio)
mostrar_grafo(grafo, distancias)
