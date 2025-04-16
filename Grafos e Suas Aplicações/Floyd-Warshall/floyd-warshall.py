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

"""
📝 Exercício:
Dado um grafo com 4 vértices, utilize o algoritmo de Floyd-Warshall para:
	1.	Calcular as menores distâncias.
	2.	Exibir o caminho mais curto de cada par de vértices.

Entrada:

graph = [
    [0,   1,   4, INF],
    [INF, 0,   2, INF],
    [INF, INF, 0, 3],
    [INF, INF, INF, 0]
]
"""

"""
1️⃣ Criar a matriz de next (próximo passo no caminho)

Essa matriz serve para reconstruir os caminhos. Se o caminho direto de i a j existe inicialmente, colocamos next[i][j] = j. Se não houver caminho direto, deixamos como None.

2️⃣ Durante as atualizações de distância, atualizar também next[i][j]

Se encontramos um caminho melhor passando por k, fazemos:

    next[i][j] = next[i][k]
    
Isso quer dizer: “Para ir de i até j, primeiro vá para onde você iria a partir de i até k”.

3️⃣ Reconstruir o caminho entre i e j

Usamos a matriz next para montar o caminho passo a passo, até chegar em j.
"""

INF = float('inf')

def floyd_warshall_with_path(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    next_node = [[None if graph[i][j] == INF else j for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]

    return dist, next_node

def reconstruct_path(u, v, next_node):
    if next_node[u][v] is None:
        return []
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path

# 🧪 Exemplo de uso

graph = [
    [0,   3,   INF, 5],
    [2,   0,   INF, 4],
    [INF, 1,   0,   INF],
    [INF, INF, 2,   0]
]

dist, next_node = floyd_warshall_with_path(graph)

print("")
print("Reconstruct path:")
# Exibir caminho e distância entre todos os pares
for i in range(len(graph)):
    for j in range(len(graph)):
        if i != j:
            path = reconstruct_path(i, j, next_node)
            if path:
                print(f"Caminho de {i} a {j}: {path} | Distância: {dist[i][j]}")
            else:
                print(f"Não há caminho de {i} a {j}")


"""
Adaptando para grafos não-direcionados:

🧠 Lembrete rápido: Grafo não direcionado

Um grafo não direcionado é aquele onde a aresta entre u e v implica que há conexão nos dois sentidos:
Se há aresta u → v, também há v → u.

🛠️ Passos para adaptar
	1.	Construir a matriz de adjacência simétrica:
    Para cada aresta (u, v) com peso w, atribuímos:

        graph[u][v] = w
        graph[v][u] = w
    
	2.	Executar o Floyd-Warshall normalmente:
    O algoritmo funciona do mesmo jeito, porque ele opera sobre a matriz. A diferença é só garantir que a entrada seja simétrica.
"""
INF = float('inf')

def floyd_warshall_with_path(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    next_node = [[None if graph[i][j] == INF else j for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]

    return dist, next_node

def reconstruct_path(u, v, next_node):
    if next_node[u][v] is None:
        return []
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path

"""
Detecção de ciclos negativos:

O algoritmo de Floyd-Warshall pode detectar ciclos negativos ao verificar a diagonal principal da matriz de distâncias:
	•	Se qualquer dist[i][i] < 0, isso indica que há um ciclo negativo acessível a partir do vértice i.
"""

INF = float('inf')

def floyd_warshall_with_negative_cycle_detection(graph):
    n = len(graph)
    dist = [row[:] for row in graph]  # cópia da matriz

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Verifica ciclos negativos na diagonal
    for i in range(n):
        if dist[i][i] < 0:
            return True  # Ciclo negativo detectado

    return False

"""
Matriz de predecessores:
    A matriz de predecessores (pred) no algoritmo de Floyd-Warshall é usada para reconstruir os caminhos mínimos entre pares de vértices.
    
🧠 O que é a matriz de predecessores?
	•	pred[i][j] guarda o vértice anterior a j no caminho mínimo de i até j.
	•	Inicialmente:
	•	Se houver uma aresta direta de i para j, então pred[i][j] = i.
	•	Se i == j, então pred[i][j] = None.
	•	Se não há caminho direto, então pred[i][j] = None.

Durante o algoritmo:
	•	Se o caminho i → k → j for mais curto que o atual i → j, então:
	•	pred[i][j] = pred[k][j]
	

✅ Implementação com matriz de predecessores
"""

INF = float('inf')

def floyd_warshall_with_path(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    pred = [[None for _ in range(n)] for _ in range(n)]

    # Inicialização
    for i in range(n):
        for j in range(n):
            if graph[i][j] != INF and i != j:
                pred[i][j] = i

    # Floyd-Warshall com atualização de predecessores
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        pred[i][j] = pred[k][j]

    return dist, pred

# 🔁 Função para reconstruir o caminho de u até v
def reconstruct_path(pred, u, v):
    if pred[u][v] is None:
        return []

    path = [v]
    while u != v:
        v = pred[u][v]
        path.append(v)
    path.reverse()
    return path

# 🧪 Exemplo de uso

graph = [
    [0,     3,     INF,   5],
    [2,     0,     INF,   4],
    [INF,   1,     0,     INF],
    [INF,   INF,   2,     0]
]

dist, pred = floyd_warshall_with_path(graph)

# Reconstruir o caminho de 0 até 2
path = reconstruct_path(pred, 0, 2)

print("Caminho mínimo de 0 até 2:", path)

