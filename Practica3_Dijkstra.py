# Importamos las librerías necesarias
import matplotlib.pyplot as plt
import networkx as nx

# Creamos un grafo dirigido (con flechas)
G = nx.DiGraph()

# Lista de conexiones entre nodos con sus respectivos pesos
# Cada tupla representa una conexión: (origen, destino, peso)
edges = [
    ('A', 'B', 5),
    ('A', 'C', 2),
    ('B', 'D', 1),
    ('C', 'E', 8),
    ('D', 'F', 6)
]

# Agregamos las aristas (conexiones) al grafo con su peso
for origen, destino, peso in edges:
    G.add_edge(origen, destino, weight=peso)

# Aplicamos el algoritmo de Dijkstra para encontrar la distancia mínima
# desde el nodo 'A' a todos los demás nodos
shortest_path = nx.single_source_dijkstra_path_length(G, 'A')

# Calculamos posiciones para dibujar los nodos distribuidos de forma clara
# 'spring_layout' es un diseño que intenta separar los nodos de forma automática
pos = nx.spring_layout(G, seed=42)  # seed hace que sea reproducible

# Dibujamos los nodos con color azul claro y tamaño grande
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=1500)

# Dibujamos las flechas que representan las conexiones (aristas) entre nodos
nx.draw_networkx_edges(G, pos, arrowstyle='-|>', arrowsize=20)

# Creamos las etiquetas para cada nodo:
# Mostramos el nombre del nodo y la distancia desde el nodo inicial (A)
node_labels = {nodo: f"{nodo}\n{shortest_path.get(nodo, '∞')}" for nodo in G.nodes()}
nx.draw_networkx_labels(G, pos, labels=node_labels, font_size=10, font_weight='bold')

# Obtenemos los pesos de las aristas para mostrarlos como etiquetas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# Título del gráfico
plt.title("Algoritmo de Dijkstra desde el nodo A")

# Quitamos los ejes para que el grafo se vea más limpio
plt.axis('off')

# Ajustamos automáticamente el contenido del gráfico
plt.tight_layout()

# Mostramos el gráfico en pantalla
plt.show()
