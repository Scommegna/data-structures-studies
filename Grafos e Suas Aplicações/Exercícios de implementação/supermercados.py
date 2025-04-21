"""
Um supermercado, localizado na cidade de Drummondville (Québec, Canadá), iniciou suas atividades recentemente e tem se destacado pela preocupação com o bem-estar de seus empregados. A empresa pretende comprar um ônibus para o transporte dos funcionários. Por ser uma cidade de pequeno porte, todas as ruas de Drummondville são de mão-dupla.  O supermercado, desejando reduzir os custos, quer saber qual é o número mínimo de viagens que um motorista deve fazer para sair de um ponto A, levar os funcionários para um ponto B, considerando um total de C funcionários a serem transportados. Existe uma capacidade máxima permitida para o transporte de passageiros em cada rua de Drummonville. Essa última restrição é uma exigência recente da prefeitura, para preservar a arquitetura histórica da cidade e conservar mais as vias de circulação.

Como exemplo, suponha que as ruas, com as suas devidas intersecções e limite máximo de passageiros, sejam apresentadas abaixo:

(1,2): máximo de 30 pessoas;(1,3): máximo de 20 pessoas;(1,4): máximo de 10 pessoas;(2,4): máximo de 40 pessoas;(2,5): máximo de 80 pessoas;(3,4): máximo de 13 pessoas;(3,6): máximo de 13 pessoas;(4,7): máximo de 25 pessoas;(5,7): máximo de 12 pessoas;(6,7): máximo de 35 pessoas.

Considerando A = 1, B = 7 e C = 97, então o supermercado gastaria pelo menos 5 viagens para levar todos os seus funcionários ao destino, levando em conta uma aquisição de um ônibus que carregue até 25 pessoas.

Entrada

A entrada do problema pode conter um ou mais casos de teste. Para cada caso de teste, a primeira linha contém dois inteiros: o número de intersecções da cidade, X, e o número de ruas da cidade, denotada por Y. As próximas Y linhas contém, cada uma, três inteiros: u, v e p, correspondendo à intersecção u que liga à intersecção v, com limite máximo de pessoas dentro de um veículo de transporte dado por p. Na linha subsequente, considera-se os valores de A, B e C, respectivamente. O fim de todos os casos de teste é dado pela sequência de dois zeros.

Saída

Para cada caso de teste, imprima o número mínimo de viagens necessárias para transportar os funcionários do supermercaso.

Samples Input:

7 10
1 2 30
1 3 20
1 4 10
2 4 40
2 5 80
3 4 13
3 6 13
4 7 25
5 7 12
6 7 35
1 7 97
0 0

Samples Output
5
"""

import math
import heapq

import sys

def dijkstra_with_max_capacity(input_graph, start_index, end_index, n):
    visited_nodes = [False] * (n + 1)

    max_capacity = [0] * (n + 1)
    max_capacity[start_index] = float('inf')

    heap = [(-max_capacity[start_index], start_index)]

    while heap:
        negative_cap, u = heapq.heappop(heap)
        cap = -negative_cap

        if visited_nodes[u]:
            continue
        visited_nodes[u] = True

        for v, weight in input_graph[u]:
            min_cap = min(cap, weight)
            if min_cap > max_capacity[v]:
                max_capacity[v] = min_cap
                heapq.heappush(heap, (-min_cap, v))

    return max_capacity[end_index]

def main():
    input_lines = sys.stdin.read().splitlines()

    index = 0

    while True:
        x, y = map(int, input_lines[index].split())
        index += 1
        if x == 0 and y == 0:
            break

        graph = {i: [] for i in range(1, x + 1)}

        for _ in range(y):
            u, v, p = map(int, input_lines[index].split())

            graph[u].append((v, p))
            graph[v].append((u, p))

            index += 1

        a, b, c = map(int, input_lines[index].split())
        index += 1

        cap = dijkstra_with_max_capacity(graph, a, b, x)
        util_cap = cap - 1

        number_of_travels = math.ceil(c / util_cap)
        print(number_of_travels)

if __name__ == "__main__":
    main()