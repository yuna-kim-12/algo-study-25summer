import sys
import heapq
sys.stdin = open('num.txt')

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)

        if dist > distance[node]:
            continue

        for i in graph[node]:
            cost = dist + 1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    return


INF = int(1e9)
a, b = map(int, input().split())
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)

for i in range(1, M+1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

dijkstra(a)

if distance[b] < INF:
    print(distance[b])
else:
    print(-1)