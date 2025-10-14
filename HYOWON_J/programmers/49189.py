# from collections import deque
#
# def solution(n, edge):
#     graph = [[] for _ in range(n+1)]
#     check = [-1] * (n+1)
#
#     for i, j in edge:
#         graph[i].append(j)
#         graph[j].append(i)
#
#     def BFS(node):
#         que = deque()
#         que.append(node)
#         check[node] += 1
#
#         while que:
#             now = que.popleft()
#             for next in graph[now]:
#                 if check[next] < 0:
#                     check[next] = check[now] + 1
#                     que.append(next)
#         return
#
#     BFS(1)
#
#     return check.count(max(check))

import heapq

def solution(n, edge):
    answer = 0
    g = [[] for _ in range(n + 1)]
    INF = int(1e9)
    v = [INF] * (n + 1)

    for i in edge:
        a, b = i
        g[a].append(b)
        g[b].append(a)

    def dijkstra(start):
        q = []
        heapq.heappush(q,(0, start))
        v[start] = 0

        while q:
            dist, n = heapq.heappop(q)

            if dist > v[n]:
                continue

            for i in g[n]:
                cost = dist + 1
                if cost < v[i]:
                    v[i] = cost
                    heapq.heappush(q, (cost, i))
        return

    dijkstra(1)

    print(v)

    return answer

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))