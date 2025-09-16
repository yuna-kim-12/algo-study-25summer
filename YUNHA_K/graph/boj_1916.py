# import sys
# input = sys.stdin.readline
import heapq

def dijkstra(start, end):
    INF = float('inf')
    distance = [INF]*(N+1)

    queue = [(0,start)]
    distance[start] = 0
    while queue:
        dist, cur_node = heapq.heappop(queue)

        if cur_node == end:
            return dist

        if dist > distance[cur_node]:
            continue

        for next_dist, next_node in graph[cur_node]:
            dist_sum = next_dist + distance[cur_node]
            if dist_sum < distance[next_node]:
                distance[next_node] = dist_sum
                heapq.heappush(queue,(dist_sum, next_node))


    return distance[end]


# 입력
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

S, D = map(int, input().split())

print(dijkstra(S,D))