import sys, heapq
sys.stdin = open('5972.txt')

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    root = []

    while q:
        dist, now = heapq.heappop(q)

        if dist > distances[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return



N, M = map(int, input().split())
INF = int(1e9)
distances = [INF] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

dijkstra(1)

print(distances[N])