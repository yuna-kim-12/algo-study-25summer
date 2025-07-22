import sys
def bfs(start_node, visited:list, lst:list):
    from collections import deque
    queue = deque([start_node])
    visited[start_node] = 1
    count = 0

    while queue:
        a = queue.popleft()
        count += 1
        for next_node in lst[a]:
            if not visited[next_node]:
                visited[next_node] = 1
                queue.append(next_node)

    return count -1

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

lst = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

visited = [0 for _ in range(N+1)]

answer = bfs(1, visited, lst)
print(answer)