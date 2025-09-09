import heapq

INF = float('inf')
# 0번 지점에서 N번 지점까지 이동하는데 걸리는 최소 거리
# 다익스트라 알고리즘
def dijkstra(start_node):
    # 시작점
    heap = [(0, start_node)]
    distance = [INF for _ in range(N+1)]
    distance[start_node] = 0

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)

        if cur_node == N:
            return cur_dist

        if cur_dist > distance[cur_node]:
            continue

        for next_node, next_node_dist in graph[cur_node]:
            next_dist = cur_dist + next_node_dist
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heapq.heappush(heap, (next_dist, next_node))

    return distance[N]

# 입력
T = int(input())
for tc in range(1,T+1):
    N, E = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    result = dijkstra(0)
    print(f'#{tc} {result}')