import sys
from collections import deque
sys.stdin = open('n.txt')


n = int(input())
arr = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_h = 0
answer = 0

def bfs(i, j, rain):
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            xx = dx[i] + x
            yy = dy[i] + y
            if 0 <= xx < n and 0 <= yy < n:
                if visited[xx][yy] == 0 and arr[xx][yy] > rain:
                    visited[xx][yy] = 1
                    q.append([xx, yy])
    return

for _ in range(n):
    a = list(map(int, input().split()))
    max_h = max(max_h, max(a))
    arr.append(a)

# 비가 내리지 않을때도 예상해야함.
for i in range(0, max_h):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(n):
            if arr[x][y] > i and visited[x][y] == 0:
                bfs(x, y, i)
                count += 1
    answer = max(answer, count)

print(answer)