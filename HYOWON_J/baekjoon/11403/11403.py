import sys
sys.stdin = open('11403.txt')

def floyd_warshall(n, graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1

    return


N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

floyd_warshall(N, graph)
for i in range(N):
    print(*graph[i])