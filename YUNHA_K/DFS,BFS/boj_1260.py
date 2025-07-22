def dfs(start_node, graph, visited, path):
    visited[start_node] = 1
    path.append(start_node)

    for next_node in graph[start_node]:
        if not visited[next_node]:
            dfs(next_node, graph, visited, path)

def bfs(start_node, graph, visited, path):
    from collections import deque
    queue = deque()
    queue.append(start_node)
    visited[start_node] = 1

    while queue:
        cur_node = queue.popleft()
        visited[cur_node] = 1
        path.append(cur_node)

        for next_node in graph[cur_node]:
            if not visited[next_node] and next_node not in queue:
                queue.append(next_node)

N, M, V = map(int, input().split())
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
path_dfs = []
path_bfs = []

for lst in graph:
    lst.sort()

dfs(V, graph, visited_dfs, path_dfs)
bfs(V, graph, visited_bfs, path_bfs)

print(*path_dfs)
print(*path_bfs)