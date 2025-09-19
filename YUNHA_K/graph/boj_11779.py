# import sys
# input = sys.stdin.readline
import heapq

def dijkastra(start_node, end_node):
    distance = [INF]*(N+1)
    parent= [-1]*(N+1)
    queue = [(0,start_node)]
    distance[start_node] = 0

    while queue:
        weight, cur_node = heapq.heappop(queue)

        if cur_node == end_node:
            break

        if weight > distance[cur_node]:
            continue

        for next_node, next_weight  in graph[cur_node]:
            total_weight = next_weight + weight
            if distance[next_node] > total_weight:
                distance[next_node] = total_weight
                parent[next_node] = cur_node
                heapq.heappush(queue, (total_weight, next_node))

    path = []
    current = end_node
    while current != -1:
        path.append(current)
        current = parent[current]
    path.reverse()
    return distance[end_node], path

N = int(input())
m = int(input())
graph = [[] for _ in range(N+1)]
INF = float('inf')
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
S, E = map(int, input().split())
weight, path = dijkastra(S,E)
print(weight)
print(len(path))
print(*path)