"""
📌 Definição:

O algoritmo de Bellman-Ford calcula o caminho de custo mínimo de um vértice de origem para todos os outros vértices em um grafo ponderado, mesmo se houver arestas com pesos negativos.

✅ Ao contrário de Dijkstra, o Bellman-Ford funciona mesmo com pesos negativos.

⚠️ Se houver ciclos negativos acessíveis a partir da origem, o algoritmo detecta isso.

🧠 Complexidade:
	•	Tempo: O(V * E) onde V = vértices, E = arestas.
	•	Espaço: O(V)

✅ Implementação (lista de adjacência):
"""

def bellman_ford(graph, V, start):
    dist = [float('inf')] * V
    dist[start] = 0

    for _ in range(V - 1):
        for u in range(V):
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

    # Verifica ciclo negativo
    for u in range(V):
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                print("Ciclo negativo detectado!")
                return None

    return dist

graph = {
    0: [(1, 4), (2, 5)],
    1: [(2, -3)],
    2: [(3, 4)],
    3: []
}

dist = bellman_ford(graph, 4, 0)
print("Distâncias mínimas:", dist)

# Distâncias mínimas: [0, 4, 1, 5]

# 💡 Como reconstruir caminhos?

def get_path(predecessor, target):
    path = []
    while target is not None:
        path.append(target)
        target = predecessor[target]
    return path[::-1]

"""
🧱 Matriz de Adjacência:

Você pode converter para lista de arestas:
"""

matrix = [
    [0, 4, 5, float('inf')],
    [float('inf'), 0, -3, float('inf')],
    [float('inf'), float('inf'), 0, 4],
    [float('inf'), float('inf'), float('inf'), 0]
]

# Converte para lista de adjacência
graph = {i: [] for i in range(4)}
for i in range(4):
    for j in range(4):
        if matrix[i][j] != float('inf') and i != j:
            graph[i].append((j, matrix[i][j]))

"""
🧩 Exercícios (Simples a Intermediário)
	1.	✅ [Simples] Dado um grafo com pesos (incluindo negativos), encontre o menor caminho de um vértice de origem para os demais.
	2.	✅ [Intermediário] Modifique o algoritmo de Bellman-Ford para detectar ciclos negativos.
	3.	✅ [Intermediário] Adapte a solução para também reconstruir o caminho do vértice de origem até os demais.
"""

# 📘 EXERCÍCIO 1: Encontrar o menor caminho

def bellman_ford(graph, V, start):
    distance = [float('inf')] * V
    distance[start] = 0

    for _ in range(V - 1):
        for u, v, w in graph:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    return distance

# Exemplo de uso:
graph = [
    (0, 1, 4),
    (0, 2, 5),
    (1, 2, -3),
    (2, 3, 4),
    (3, 1, -6)
]

V = 4
start = 0
print(bellman_ford(graph, V, start))

# 📘 EXERCÍCIO 2: Detectar ciclos negativos

def has_negative_cycle(graph, V, start):
    distance = [float('inf')] * V
    distance[start] = 0

    for _ in range(V - 1):
        for u, v, w in graph:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    # Verifica ciclo negativo
    for u, v, w in graph:
        if distance[u] + w < distance[v]:
            return True

    return False

# Exemplo com ciclo negativo:
graph = [
    (0, 1, 1),
    (1, 2, -1),
    (2, 0, -1)
]

print(has_negative_cycle(graph, 3, 0))  # True

# 📘 EXERCÍCIO 3: Reconstruir caminhos

def bellman_ford_with_path(graph, V, start):
    distance = [float('inf')] * V
    predecessor = [None] * V
    distance[start] = 0

    for _ in range(V - 1):
        for u, v, w in graph:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u

    def build_path(v):
        path = []
        while v is not None:
            path.append(v)
            v = predecessor[v]
        return path[::-1]

    paths = {v: build_path(v) if distance[v] != float('inf') else None for v in range(V)}
    return distance, paths

# Exemplo:
graph = [
    (0, 1, 1),
    (1, 2, 2),
    (0, 2, 10),
    (2, 3, 1)
]

distance, paths = bellman_ford_with_path(graph, 4, 0)

print("Distâncias:", distance)
print("Caminhos:")
for v in range(4):
    print(f"0 -> {v}: {paths[v]}")

# 📌 Saída esperada:

"""
Distâncias: [0, 1, 3, 4]
Caminhos:
0 -> 0: [0]
0 -> 1: [0, 1]
0 -> 2: [0, 1, 2]
0 -> 3: [0, 1, 2, 3]
"""