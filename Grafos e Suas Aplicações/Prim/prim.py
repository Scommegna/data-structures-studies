"""
🌳 Definição

O Algoritmo de Prim encontra uma árvore geradora mínima (MST) de um grafo conexo, não direcionado e ponderado, ou seja:
	•	Uma árvore que conecta todos os vértices com o menor custo total possível.
	•	Ele cresce a MST adicionando, a cada passo, a menor aresta que conecta um vértice já na árvore a um vértice fora dela.

✅ Implementação com Lista de Adjacência
"""

import heapq

def prim(graph, start):
    visited = set()
    mst = []
    min_heap = [(0, start, None)]  # (peso, atual, origem)
    total_cost = 0

    while min_heap:
        cost, current, parent = heapq.heappop(min_heap)
        if current not in visited:
            visited.add(current)
            total_cost += cost
            if parent is not None:
                mst.append((parent, current, cost))

            for neighbor, weight in graph[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, current))

    return mst, total_cost

# 🔹 Exemplo de grafo com lista de adjacência

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}

mst, cost = prim(graph, 0)
print("Arestas da MST:", mst)
print("Custo total:", cost)

# ✅ Implementação com Matriz de Adjacência

def prim_matrix(graph):
    n = len(graph)
    selected = [False] * n
    parent = [-1] * n
    key = [float('inf')] * n
    key[0] = 0

    for _ in range(n):
        u = min((v for v in range(n) if not selected[v]), key=lambda x: key[x])
        selected[u] = True

        for v in range(n):
            if graph[u][v] != 0 and not selected[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    mst = []
    total_cost = 0
    for i in range(1, n):
        mst.append((parent[i], i, graph[i][parent[i]]))
        total_cost += graph[i][parent[i]]

    return mst, total_cost

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

mst, cost = prim_matrix(graph)
print("Arestas da MST:", mst)
print("Custo total:", cost)


"""
📝 Exercícios Simples
	1.	[Fácil] Dado um grafo com 4 vértices e as seguintes arestas:
	
	(0-1, 10), (0-2, 6), (0-3, 5), (1-3, 15), (2-3, 4)
	
➤ Encontre a MST usando Prim.
"""

input_graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)],
}

def prim(graph_adjlist, start):
    visited = set()
    mst = []
    min_heap = [(0, start, None)]
    total_cost = 0

    while min_heap:
        cost, current, parent = heapq.heappop(min_heap)

        if current not in visited:
            visited.add(current)
            total_cost += cost

            if parent is not None:
                mst.append((parent, current, cost))

            for neighbor, weight in graph_adjlist[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, current))

    return mst, total_cost

mst_exercise, exercise_totalcost = prim(input_graph, 0)

print("Exercise 1:")
print("Total cost:" , exercise_totalcost)
print("MST: ", mst_exercise)
