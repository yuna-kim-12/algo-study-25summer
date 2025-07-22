import sys
sys.stdin = open('num.txt')
from collections import deque

K = int(input())

def BFS(arr, V):
    check = [0] * (V + 1)

    for start in range(1, V+1):
        if check[start] == 0:
            q = deque()
            q.append(start)
            check[start] = 1

            while q:
                now = q.popleft()
                for next in arr[now]:
                    if check[next] == 0:
                        q.append(next)
                        check[next] = -check[now]
                    elif check[next] == check[now]:
                        return "NO"

    return 'YES'

for _ in range(K):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]

    for _ in range(E):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)

    print(BFS(arr, V))
