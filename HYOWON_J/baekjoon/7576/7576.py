from collections import deque
import sys
sys.stdin = open('n.txt')

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
           q.append([i,j])

while q:
    x, y = q.popleft()
    for i in range(4):
        di = x + dx[i]
        dj = y + dy[i]
        if 0 <= di < n and 0 <= dj < m and box[di][dj] == 0:
            box[di][dj] = box[x][y] + 1
            q.append([di, dj])


answer = 0
for i in box:
    if 0 in i :
        print(-1)
        exit()
    answer = max(answer, max(i))

print(answer - 1)