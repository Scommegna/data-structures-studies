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
from os.path import pathsep


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

"""
✅ O que são componentes conectados em um grafo?

📌 Definição (grafo não direcionado):

Um componente conectado é um subconjunto de vértices de um grafo não direcionado onde:
	•	Qualquer vértice pode ser alcançado a partir de qualquer outro dentro do mesmo componente.
	•	E não existe nenhuma conexão com vértices fora desse subconjunto.

Em outras palavras:

Um componente conectado é uma “ilha” dentro do grafo onde todos os vértices estão conectados entre si, mas não com vértices de outras “ilhas”.


🧭 Definição (grafo direcionado):

Em um grafo direcionado, há dois tipos:
	•	Componente fortemente conectado: todos os vértices do componente são acessíveis entre si em ambas as direções.
	•	Componente fracamente conectado: se ignorarmos a direção das arestas, todos os vértices estariam conectados.
	
📊 Exemplo (grafo não direcionado)

Imagine o grafo:

0 —— 1      3 —— 4      5
     |              
     

	•	Componente 1: {0, 1}
	•	Componente 2: {3, 4}
	•	Componente 3: {5} (vértice isolado)

    Total: 3 componentes conectados
    

💡 Como encontrar componentes conectados?

Usamos algoritmos como:
	•	BFS (Busca em Largura)
	•	DFS (Busca em Profundidade)

Cada vez que você encontra um vértice não visitado e inicia uma busca, você está entrando em um novo componente.

"""

graph = {
    0: [1],
    1: [0],
    2: [3],
    3: [2, 4],
    4: [3],
    5: [],
}

def bfs(start, visited, graph):
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not neighbor in visited:
                visited.add(neighbor)
                queue.append(neighbor)

def count_connected_components(graph):
    visited = set()
    components_count = 0

    for key in graph.keys():
        if not key in visited:
            bfs(key, visited, graph)
            components_count += 1

    return components_count

print("")
print("Medium exercise: found connected components in graph:")
print(count_connected_components(graph))

# 3️⃣ (Difícil) Use BFS para encontrar o menor caminho entre dois vértices em um grafo não ponderado.
def bfs_for_shortest_path(start, end, graph):
    visited = set([start])
    paths = {start: [start]}
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                paths[neighbor] = paths[current] + [neighbor]
                queue.append(neighbor)

    if end in paths:
        return paths[end]

    return None

first_input = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2, 4],
    4: [3]
}

print("")
print("output for hard exercise of find shortest path between nodes")
print(bfs_for_shortest_path(0, 4, first_input))