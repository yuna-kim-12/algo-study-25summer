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

        for i in village[node]:
            cost = dist + i[1]
            if cost < distances[i[0]]:
                distances[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return


N = int(input())
M = int(input())
INF = int(1e9)
distances = [INF] * (N+1)

village = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, d = map(int, input().split())
    village[s].append([e, d])

start, end = map(int, input().split())

dijkstra(start)

print(distances[end])