import sys
from collections import deque
sys.stdin = open('n.txt')

n = int(input())
arr = []
visited = [[0 for _ in range(n)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for _ in range(n):
    arr.append(list(map(int, input())))

def bfs(i, j):
    visited[i][j] = count
    q = deque()
    q.append([i, j])

    while q:
        x, y = q.popleft()
        for i in range(4):
            xxx = x + dx[i]
            yyy = y + dy[i]
            if 0 <= xxx < n and 0 <= yyy < n:
                if visited[xxx][yyy] == 0 and arr[xxx][yyy]:
                    visited[xxx][yyy] = count
                    q.append([xxx, yyy])
    return

count = 0
for i in range(n):
    for j in range(n):
        if arr[i][j] and visited[i][j] == 0:
            count += 1
            bfs(i, j)

print(count)
dict = {}
for i in range(count+1):
    dict[i]= 0

for i in range(n):
    for j in range(n):
        dict[visited[i][j]] += 1

for s in sorted(dict[i] for i in range(1, count+1)):
    print(s)