"""
📘 Definição

O algoritmo de Floyd-Warshall é um algoritmo para encontrar o menor caminho entre todos os pares de vértices em um grafo ponderado (com pesos), que pode ser direcionado ou não.
Ele também pode detectar ciclos negativos.
	•	🟢 Funciona com grafos com arestas negativas, mas não com ciclos negativos.
	•	⏱️ Complexidade: O(V³), onde V é o número de vértices.

✅ Aplicações
	•	Encontrar todas as distâncias mínimas entre pares de cidades.
	•	Resolver problemas de roteamento em redes.
	•	Detectar se existe caminho negativo (distância menor que zero entre um nó e ele mesmo).

🧠 Ideia principal

A ideia é usar programação dinâmica:
	•	dist[i][j] começa com o peso direto da aresta de i para j (ou ∞ se não existe).
	•	Gradualmente atualizamos dist[i][j] usando vértices intermediários k.

Relação de recorrência:
    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
"""

# 🧩 Implementação em Matriz de Adjacência (mais comum):

INF = float('inf')

def floyd_warshall(graph):
    V = len(graph)
    dist = [row[:] for row in graph]  # cópia da matriz original

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# 🧪 Exemplo:
graph = [
    [0,   3,   INF, 5],
    [2,   0,   INF, 4],
    [INF, 1,   0,   INF],
    [INF, INF, 2,   0]
]

result = floyd_warshall(graph)

for row in result:
    print(row)

"""
🔢 Saída:

[0, 3, 7, 5]
[2, 0, 6, 4]
[3, 1, 0, 5]
[5, 3, 2, 0]
"""

"""
🔁 Implementação com Lista de Adjacência

Floyd-Warshall precisa de matriz para funcionar bem. Se tiver uma lista de adjacência, primeiro converta-a para uma matriz de adjacência com pesos.
"""

"""
✍️ Exercício Simples

Exercício 1:
Dado o grafo com 4 vértices e a seguinte matriz de adjacência (com pesos), use o algoritmo de Floyd-Warshall para encontrar todas as menores distâncias:
"""

graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

# Saída esperada:
"""
[0, 5, 8, 9]
[INF, 0, 3, 4]
[INF, INF, 0, 1]
[INF, INF, INF, 0]
"""

def floyd_warshall(input_graph):
    n = len(input_graph)

    dist_matrix = [row[:] for row in input_graph ]

    for k in range(n):
        for j in range(n):
            for i in range(n):
                if dist_matrix[i][k] + dist_matrix[k][j] < dist_matrix[i][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]

    return dist_matrix

print("")
print("First Exercise:")

resp = floyd_warshall(graph)


for row in resp:
    print(row)

"""
📘 Exemplos práticos onde Floyd-Warshall é usado e BFS falha:

1. 🔁 Todos os pares de menores caminhos:

Imagine um sistema onde você quer saber a distância mais curta entre todos os pares de cidades (como em mapas, GPS ou redes).
	•	Floyd-Warshall resolve isso com uma única execução.
	•	BFS teria que ser executado uma vez para cada vértice e não funcionaria se houver pesos diferentes nas arestas.
	

2. ⛔ Presença de pesos negativos:

Se o grafo tiver pesos negativos (por exemplo, representar descontos, perdas ou penalidades):
	•	Floyd-Warshall funciona (desde que não haja ciclos negativos).
	•	BFS assume peso constante (geralmente 1), então não pode lidar com pesos.
	
3. 🔍 Detecção de ciclos negativos:
	•	Floyd-Warshall detecta ciclos negativos ao verificar se dist[i][i] < 0 para algum vértice i.
	•	BFS não pode detectar ciclos negativos porque não lida com pesos.
	
✅ Quando usar BFS então?
	•	Para encontrar o menor caminho em grafos não ponderados (peso = 1 em todas as arestas).
	•	Para descobrir conectividade, componentes, níveis ou distâncias mínimas a partir de uma única origem em grafos simples.
"""

"""
📌 Floyd-Warshall: Extensões e Aplicações

1️⃣ Adaptar o algoritmo para rastrear os caminhos

Conceito:
Além de calcular as menores distâncias, podemos também reconstruir o caminho real entre dois vértices.

Como fazer:
Criamos uma matriz next[i][j] que armazena o próximo vértice no caminho de i para j.
Se next[i][j] = k, isso significa que, para ir de i a j, o primeiro passo é para k.

Exemplo de inicialização:

# Caminho direto
if graph[i][j] != INF:
    next[i][j] = j
else:
    next[i][j] = None
"""

# Para reconstruir o caminho de i até j:
def construct_path(i, j, next):
    if next[i][j] is None:
        return []

    path = [i]
    while i != j:
        i = next[i][j]
        path.append(i)
    return path


