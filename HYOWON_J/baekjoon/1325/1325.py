import sys
sys.stdin = open('n.txt')
from collections import deque

N, M = map(int, input().split())
A = [[] for _ in range(N+1)]
check = [-1] * (N+1)
answer = []
max_cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    A[b].append(a)

def BFS(start):
    global max_cnt
    visited = [False] * (N+1)
    arr = deque()
    arr.append(start)
    visited[start] = True
    cnt = 0
    while arr:
        now = arr.popleft()
        for i in A[now]:
            if check[i] == -1:
                arr.append(i)
                visited[i] = True
                cnt += 1

    check[start] = cnt
    max_cnt = max(max_cnt, cnt)
    return

for i in range(1, N+1):
    BFS(i)

for i in range(len(check)):
    if max_cnt == check[i]:
        answer.append(i)

print(*answer)