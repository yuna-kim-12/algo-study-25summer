import sys
sys.stdin = open('1956.txt')

V, E = map(int, input().split())
INF = int(1e9)
graph = [[INF]*(V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

#거리가 최소 인지?
for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

#왕복 가능한지?
answer = INF
for i in range(1, V+1):
    for j in range(1, V+1):
        answer = min(answer, graph[i][j] + graph[j][i])

if answer == INF:
    print(-1)
else:
    print(answer)
