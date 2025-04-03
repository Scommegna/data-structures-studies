"""
📌 Matriz de Adjacência em Grafos

A Matriz de Adjacência é uma representação de um grafo em que cada posição [i][j] da matriz indica se existe uma aresta entre os vértices i e j.

📝 Exemplo 1: Grafo Não Direcionado

🔹 Grafo Representado:
    (0) --- (1)
      \     /
       (2)
       
🔹 Matriz de Adjacência:

    0 1 2
    0 0 1 1
    1 1 0 1
    2 1 1 0
"""

# 🔹 Código em Python:

class Graph:
    def __init__(self, vertexes):
        self.V = vertexes
        self.matrix = [[0] * vertexes for _ in range(vertexes)]
        
    def add_edge(self, v1, v2):
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1 # Não direcionado
        
    def print_graph(self):
        for row in self.matrix:
            print(row)
            
# Criando o grafo
g = Graph(3)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)

# Imprimindo a matriz
g.print_graph()

"""
📝 Exemplo 2: Grafo Direcionado

🔹 Grafo Representado:

    (0) → (1)
     ↓  
    (2)
    
🔹 Matriz de Adjacência:

      0 1 2
    0 0 1 1
    1 0 0 0
    2 0 0 0
"""

# 🔹 Código em Python:

class DirectedGraph:
    def __init__(self, vertexes):
        self.V = vertexes
        self.matrix = [[0] * vertexes for _ in range(vertexes)]
        
    def add_edge(self, v1, v2):
        self.matrix[v1][v2] = 1 # Somente a direção v1 -> v2
        
    def print_graph(self):
        for row in self.matrix:
            print(row)
            
# Criando o grafo direcionado
g = DirectedGraph(3)
g.add_edge(0, 1)
g.add_edge(0, 2)

# Imprimindo a matriz
g.print_matrix()

"""
🎯 Exercícios Simples

Exercício 1:

Implemente um grafo não direcionado com 4 vértices e as conexões:

(0) - (1)
 |  \  |
(2) - (3)
"""

g = [
    [0, 1, 1, 1],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 1, 1, 0]
]

"""
Exercício 2:

Implemente um grafo direcionado onde:

(0) → (1) → (2)
       ↓
      (3)
"""

g = [
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]