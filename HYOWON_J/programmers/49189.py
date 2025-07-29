from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    check = [-1] * (n+1)

    for i, j in edge:
        graph[i].append(j)
        graph[j].append(i)

    def BFS(node):
        que = deque()
        que.append(node)
        check[node] += 1

        while que:
            now = que.popleft()
            for next in graph[now]:
                if check[next] < 0:
                    check[next] = check[now] + 1
                    que.append(next)
        return

    BFS(1)

    return check.count(max(check))

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))