import sys
input = sys.stdin.readline

def dijkstra(start_node):
    import heapq
    distance[start_node] = 0
    hq = []
    heapq.heappush(hq,(0, start_node))

    while hq:
        weight, cur_node = heapq.heappop(hq)

        if weight > distance[cur_node]:
            continue

        for next in graph[cur_node]:
            next_weight = next[1]
            next_node = next[0]
            total_weight = weight + next_weight
            if total_weight < distance[next_node]:
                distance[next_node] = total_weight
                heapq.heappush(hq,(total_weight, next_node))

# 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하라.
# 모든 간선의 가중치 : 10 이하 자연수 -> 다익스트라.

V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]
INF = float('INF')
distance = [INF]*(V+1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))


# 출력 : V개의 줄에 걸쳐 i번째 줄에 i번 정점으로의 최단 경로의 경로값 출력.
# 시작점은 0으로 출력, 경로가 존재하지 않는 경우 "INF" 출력
dijkstra(K)
for i in range(1,V+1):
    print(distance[i]) if distance[i] != INF else print("INF")