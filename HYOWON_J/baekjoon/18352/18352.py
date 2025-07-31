import sys
sys.stdin = open('num.txt')
from collections import deque

N, M, K, X = map(int, input().split())
arr = [[] for _ in range(N+1)]
check = [-1] * (N+1)
answer = []

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

def BFS(start):
    map_node = deque()
    map_node.append(start)
    check[start] += 1
    while map_node:
        now_node = map_node.popleft()
        for i in arr[now_node]:
            if check[i] == -1:
                check[i] = check[now_node] + 1
                map_node.append(i)

BFS(X)

for i in range(len(check)):
    if check[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)