# import sys
# def bfs(start_node, visited:완전탐색, lst:완전탐색):
#     from collections import deque
#     queue = deque([start_node])
#     visited[start_node] = 1
#     count = 0
#
#     while queue:
#         a = queue.popleft()
#         count += 1
#         for next_node in lst[a]:
#             if not visited[next_node]:
#                 visited[next_node] = 1
#                 queue.append(next_node)
#
#     return count -1
#
# N = int(sys.stdin.readline())
# M = int(sys.stdin.readline())
#
# lst = [[] for _ in range(N+1)]
# for _ in range(M):
#     x, y = map(int, input().split())
#     lst[x].append(y)
#     lst[y].append(x)
#
# visited = [0 for _ in range(N+1)]
#
# answer = bfs(1, visited, lst)
# print(answer)














import sys
from collections import  deque

input = sys.stdin.readline
def bfs(start_node):
    visited = [0]*(N+1)
    queue = deque([start_node])
    visited[start_node] = 1

    while queue:
        cur_node = queue.popleft()

        for next_node in graph[cur_node]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = 1

    return visited.count(1)

# 입력
N = int(input()) # 컴퓨터의 수
graph = [[] for _ in range(N+1)]
M = int(input()) # 연결된 컴퓨터 쌍의 수
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

print(bfs(1)-1)