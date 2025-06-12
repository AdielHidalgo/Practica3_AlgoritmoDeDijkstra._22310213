import heapq

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    visitados = set()
    cola = [(0, inicio)]

    print(f"\nInicio en el nodo: {inicio}\n")

    while cola:
        distancia_actual, nodo_actual = heapq.heappop(cola)

        if nodo_actual in visitados:
            continue

        print(f"Visitando nodo {nodo_actual} con distancia acumulada {distancia_actual}")
        visitados.add(nodo_actual)

        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                heapq.heappush(cola, (nueva_distancia, vecino))
                print(f" → Se actualiza distancia de {vecino} a {nueva_distancia}")
        
        print(f"Estado actual de distancias: {distancias}\n")

    print("Distancias finales más cortas desde el nodo", inicio)
    for nodo, distancia in distancias.items():
        print(f"{inicio} → {nodo} = {distancia}")

# Ejemplo de grafo
grafo = {
    'A': {'B': 5, 'C': 1},
    'B': {'A': 5, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
    'E': {'C': 8, 'D': 3},
    'F': {'D': 6}
}

dijkstra(grafo, 'A')
