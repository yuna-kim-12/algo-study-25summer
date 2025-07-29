def bfs(start, end):
    from collections import deque
    queue = deque()
    depth = 0
    queue.append([start, depth])
    visited[start] = 1

    while queue:
        cur_node, depth = queue.popleft()
        if cur_node == end:
            return depth

        for next_node in graph[cur_node]:
            if not visited[next_node]:
                queue.append([next_node, depth+1])
                visited[next_node] = 1

    return 0

# 입력
T = int(input())
for t in range(1,T+1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    S, G = map(int, input().split())

    answer = bfs(S, G)
    print(f"#{t}", answer)