"""
📌 Algoritmo BFS (Breadth-First Search)

O BFS (Busca em Largura) é um algoritmo para percorrer ou buscar em um grafo. Ele explora todos os vértices em largura, ou seja, visita primeiro todos os vizinhos de um nó antes de avançar para os próximos níveis.

💡 Características do BFS
	•	Utiliza fila (FIFO - Primeiro a Entrar, Primeiro a Sair).
	•	Garante o caminho mais curto em um grafo não ponderado.
	•	É útil para:
	•	Encontrar caminhos mínimos.
	•	Verificar a conectividade de um grafo.
	•	Resolver quebra-cabeças como o Cubo de Rubik.
"""

# ✅ 1. Implementação com Lista de Adjacência

from collections import deque

class Graph:
    def __init__(self):
        self.adj_list = {}
        
    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
            
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) #Grafo não-direcionado
        
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        
        while queue:
            node = queue.popleft()
            
            if node not in visited:
                print(node, end=" ")
                visited.add(node)
                queue.extend(self.adj_list[node])
                
# Exemplo de uso
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

print("BFS a partir do vértice 0:")
g.bfs(1)

# ✅ 2. Implementação com Matriz de Adjacência

from collections import deque

def bfs_matrix(graph, start):
    n = len(graph)
    visited = [False] * n
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if not visited[node]:
            print(node, end=" ")
            visited[node] = True
            
            for neighbor in range(n):
                if graph[node][neighbor] == 1 and not visited[neighbor]:
                    queue.append(neighbor)
    
    
# Exemplo de uso: Matriz de Adjacência
graph = [
    [0, 1, 1, 0, 0, 0, 0],  # 0 → 1, 2
    [1, 0, 0, 1, 1, 0, 0],  # 1 → 0, 3, 4
    [1, 0, 0, 0, 0, 1, 1],  # 2 → 0, 5, 6
    [0, 1, 0, 0, 0, 0, 0],  # 3 → 1
    [0, 1, 0, 0, 0, 0, 0],  # 4 → 1
    [0, 0, 1, 0, 0, 0, 0],  # 5 → 2
    [0, 0, 1, 0, 0, 0, 0]   # 6 → 2
]

print("BFS a partir do vértice 0:")
bfs_matrix(graph, 0)

"""
📝 Exercícios Simples

1️⃣ (Fácil) Dado o seguinte grafo, implemente o BFS e mostre a sequência de visita:

    (0) - (1) - (2)
    |      |
    (3)    (4)
    
Entrada: bfs(0)
Saída esperada: 0 1 3 2 4
"""

exercise_graph = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1],
    3: [0],
    4: [1]
}

exercise_graph2 = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

def bfs_adj_list(graph, start):
    visited = set()
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            
            queue.extend(graph[node])
            
def bfs_adj_matrix(graph, start):
    n = len(graph)
    visited = [False] * n
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if not visited[node]:
            print(node, end=" ")
            visited[node] = True
            
        for neighbor in range(n):
            if not visited[neighbor] and graph[node][neighbor] == 1:
                queue.append(neighbor)
            
print("------------------------------")
bfs_adj_list(exercise_graph, 0)
print("------------------------------")
bfs_adj_matrix(exercise_graph2, 0)
    
# 2️⃣ (Médio) Modifique a implementação de BFS para contar o número de componentes conectados em um grafo.