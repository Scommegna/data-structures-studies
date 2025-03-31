"""
Listas de Adjacência

Uma lista de adjacência é uma estrutura de dados usada para representar grafos. Cada vértice tem uma lista contendo os vértices vizinhos conectados por arestas.

🔹 Vantagens:
✅ Usa menos espaço para grafos esparsos.
✅ Permite percorrer os vizinhos rapidamente.
✅ Fácil de implementar com dicionários ou listas em Python.
"""

#Implementação:

class Graph:
    def __init__(self):
        self.adj_list = {} # Dicionário para armazenar a lista de adjacência
        
    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1) # Para grafos não direcionados

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])
            
#Exemplo de uso:

graph = Graph()
for v in ['A', 'B', 'C', 'D']:
    graph.add_vertex(v)
    
# Adicionando arestas
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')

# Exibindo a lista de adjacência
graph.print_graph()

#Grafo Representado

"""
    A
   / \
  B   C
   \
    D
"""

# Lista de Adjacência (Saída do Código)

"""
A -> ['B', 'C']
B -> ['A', 'D']
C -> ['A']
D -> ['B']
"""

# 📌 Exercícios Simples

"""
1️⃣ Criação de um Grafo Direcionado

🔹 Desafio: Modifique a implementação para suportar grafos direcionados (onde A → B não significa B → A).
💡 Dica: Remova a segunda inserção em adicionar_aresta.
"""

class OrientedGraph:
    def __init__(self):
        self.adj_list = {}
        
    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []
            
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])

"""
2️⃣ Verificar se Dois Vértices São Conectados

🔹 Desafio: Implemente um método sao_conectados(v1, v2) que retorne True se existir uma aresta entre v1 e v2, e False caso contrário.
💡 Dica: Verifique se v2 está na lista de v1.
"""

class GraphWithCheckConnectionMethod:
    def __init__(self):
        self.adj_list = {} # Dicionário para armazenar a lista de adjacência
        
    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = []
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1) # Para grafos não direcionados
            
    def check_connection(self, v1, v2, visited = None):
        if visited is None:
            visited = set()
        
        if v1 == v2:
            return True # Se os vértices são os mesmos, há conexão
        
        if v1 in visited:
            return False # Evita ciclos
        
        visited.add(v1)
        
        for neighbor in self.adj_list.get(v1, []):
            if self.check_connection(neighbor, v2, visited):
                return True
        
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, "->", self.adj_list[vertex])

"""
3️⃣ Implementar Busca em Profundidade (DFS)

🔹 Desafio: Implemente um método que percorra o grafo usando Busca em Profundidade (DFS) a partir de um vértice dado.
💡 Dica: Use recursão ou uma pilha.
"""