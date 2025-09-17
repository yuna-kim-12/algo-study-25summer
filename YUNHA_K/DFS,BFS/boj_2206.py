from collections import  deque
import sys
input = sys.stdin.readline

dirs = ((1,0),(-1,0),(0,1),(0,-1)) # 상하좌우 좌표

def bfs(i, j, k):
    visited = [[[0]*2 for _ in range(M)]for _ in range(N)]
    visited[0][0][0] = 1
    queue = deque([(i, j, k)])

    while queue:
        ci, cj, k = queue.popleft()

        if ci == N-1 and cj == M-1:
            return visited[N-1][M-1][k]

        for dir in dirs:
            ni, nj = ci + dir[0], cj + dir[1]
            if 0 <= ni < N and 0 <= nj < M:
                if maze[ni][nj] == 0 and not visited[ni][nj][k]:
                    visited[ni][nj][k] = visited[ci][cj][k] + 1
                    queue.append((ni, nj, k))
                elif maze[ni][nj] == 1 and k == 0 and not visited[ni][nj][1]:
                        visited[ni][nj][1] = visited[ci][cj][0] + 1
                        queue.append((ni, nj, 1))

    return -1


# 입력
N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, input().strip())))

print(bfs(0,0,0))