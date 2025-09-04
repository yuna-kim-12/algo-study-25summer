import sys, heapq
sys.stdin = open('num.txt')

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if dist > distances[node]:
            continue

        for next in graph[node]:
            cost = dist + next[0]
            if cost < distances[next[1]]:
                distances[next[1]] = cost
                heapq.heappush(q, (cost, next[1]))

    return

INF = int(1e9)
V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
distances = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

dijkstra(K)

for i in range(1, V+1):
    if distances[i] < INF:
        print(distances[i])
    else:
        print('INF')