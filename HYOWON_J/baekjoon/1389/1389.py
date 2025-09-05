import sys
sys.stdin = open('1389.txt')

def floyd_warshall(graph, n):

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    return

INF = int(1e9)
N, M = map(int, input().split())
graph = [[INF for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 자기 자신은 바로 갈 수 있음 꼭 0표시 해야함.
for i in range(N+1):
    graph[i][i] = 0

floyd_warshall(graph, N)

answer = 0
for i in range(N, 0, -1):
    s = sum(graph[i][1:])
    if s <= INF:
        INF = s
        answer = i

print(answer)