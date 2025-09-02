import sys
sys.stdin = open('11404.txt')

def floyd_warshall(n, graph):
    dist = [row[:] for row in graph]

    for k in range(1, n+1):
        for i in range(1, n+1):
            if dist[i][k] == INF:
                continue
            for j in range(1, n+1):
                if dist[k][j] == INF:
                    continue
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c

distance = floyd_warshall(n, graph)

for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
        row.append('0' if distance[i][j] == INF else str(distance[i][j]))
    print(' '.join(row))