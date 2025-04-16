"""
✅ 1. Definição

O algoritmo de Dijkstra é usado para encontrar o menor caminho (custo mínimo) entre um vértice de origem e os demais vértices em um grafo ponderado e sem pesos negativos.

🔸 2. Exemplo intuitivo

Imagine que você quer ir de uma cidade A para outras cidades gastando o menor custo possível, e cada estrada tem um custo. O Dijkstra acha esse caminho mais barato.

🛠 3. Implementações

▶️ 3.1 Lista de Adjacência (com heapq)
"""

import heapq

def dijkstra(graph, start):
    distances = {v: float('inf') for v in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_vertex = heapq.heappop(pq)

        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Exemplo:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

print(dijkstra(graph, 'A'))  # Output esperado: {'A': 0, 'B': 1, 'C': 3, 'D': 4}

# ▶️ 3.2 Matriz de Adjacência

def dijkstra_matrix(matrix, start):
    n = len(matrix)
    dist = [float('inf')] * n
    visited = [False] * n
    dist[start] = 0

    for _ in range(n):
        min_dist = float('inf')
        u = -1
        for v in range(n):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                u = v

        visited[u] = True

        for v in range(n):
            if matrix[u][v] != 0 and not visited[v]:
                dist[v] = min(dist[v], dist[u] + matrix[u][v])

    return dist

# Exemplo:
matrix = [
    [0, 1, 4, 0],
    [0, 0, 2, 5],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

print(dijkstra_matrix(matrix, 0))  # Output: [0, 1, 3, 4]

"""
📘 4. Exercícios simples

🟦 Exercício 1:

Implemente o algoritmo de Dijkstra para o seguinte grafo:

(0) --2--> (1)
 |          |
 4          1
 |          ↓
(2) <------(3)

graph = {
    0: [(1, 2), (2, 4)],
    1: [(3, 1)],
    2: [],
    3: [(2, 1)]
}
"""

def dijkstra(graph, start_node):
    distances = {v: float('inf') for v in graph}
    distances[start_node] = 0
    pq = [(start_node, 0)]

    while pq:
        current_node, current_dist = heapq.heappop(pq)

        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            dist = current_dist + weight

            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(pq, (neighbor, dist))

    return distances

example_graph = {
    0: [(1, 2), (2, 4)],
    1: [(3, 1)],
    2: [],
    3: [(2, 1)]
}

dist_list = dijkstra(example_graph, 0)

print("Exercise 1")
print(dist_list)

"""
✅ Algoritmo de Dijkstra com Caminhos

Aqui usamos:
	•	distances: armazena o custo mínimo do início até cada vértice.
	•	previous: guarda o vértice anterior no caminho mais curto.
	•	Ao final, usamos previous para reconstruir o caminho completo.
"""

import heapq

def dijkstra_with_paths(graph, start):
    distances = {v: float('inf') for v in graph}
    previous = {v: None for v in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_dist, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(pq, (distance, neighbor))

    # Reconstruindo caminhos
    paths = {}
    for vertex in graph:
        path = []
        current = vertex
        while current is not None:
            path.append(current)
            current = previous[current]
        paths[vertex] = path[::-1] if distances[vertex] != float('inf') else None

    return distances, paths

# 🧪 Exemplo de uso

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

dist, paths = dijkstra_with_paths(graph, 'A')

print("Menores distâncias:", dist)
print("Caminhos:")
for v in paths:
    print(f"A -> {v}: {paths[v]}")

# 📌 Saída esperada:
# Menores distâncias: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
# Caminhos:
# A -> A: ['A']
# A -> B: ['A', 'B']
# A -> C: ['A', 'B', 'C']
# A -> D: ['A', 'B', 'C', 'D']