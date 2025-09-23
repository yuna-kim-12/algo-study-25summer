import sys
from collections import deque
sys.stdin = open('1600.txt')

k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

dy = (1, 2, 2, 1, -1, -2, -2, -1, -1, 0, 0, 1)
dx = (-2, -1, 1, 2, 2, 1, -1, -2, 0, -1, 1, 0)


def bfs():
    visited = [[[-1] * (k + 1) for _ in range(w)] for _ in range(h)]
    deq = deque([[0, 0, 0]])  # y 좌표, x 좌표, 말 이동 수
    visited[0][0][0] = 0

    while deq:
        y, x, z = deq.popleft()
        if y == h - 1 and x == w - 1:
            return visited[y][x][z]

        if z < k:
            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx < 0 or ny >= h or nx >= w:
                    continue
                if graph[ny][nx]:
                    continue
                if visited[ny][nx][z + 1] != -1:
                    continue
                deq.append([ny, nx, z + 1])
                visited[ny][nx][z + 1] = visited[y][x][z] + 1

        for i in range(8, 12):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= h or nx >= w:
                continue
            if graph[ny][nx]:
                continue
            if visited[ny][nx][z] != -1:
                continue
            deq.append([ny, nx, z])
            visited[ny][nx][z] = visited[y][x][z] + 1

    return -1


print(bfs())
