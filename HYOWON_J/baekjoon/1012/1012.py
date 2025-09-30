import sys
sys.stdin = open('n.txt')
from collections import deque

dx = [(1,0),(-1,0),(0,1),(0,-1)]
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    count = 0

    #문제는 x,y 좌표로 주어짐 실제 풀땐 i,j로 두고 잘 두도록
    for _ in range(k):
        j, i = map(int, input().split())
        arr[i][j] = 1

    for i in range(n):
        for j in range(m):
            # 배추 심은 곳에서 BFS 시작
            if arr[i][j] == 1 and visited[i][j] == 0:
                count += 1
                visited[i][j] = 1
                q = deque()
                q.append((i,j))
                while q:
                    x, y = q.popleft()
                    for ix, jy in dx:
                        if 0 <= x + ix < n and 0 <= y + jy < m:
                            if arr[x + ix][y + jy] == 1 and visited[x + ix][y + jy] == 0:
                                visited[x + ix][y + jy] = 1
                                q.append((x + ix, y + jy))

    print(count)