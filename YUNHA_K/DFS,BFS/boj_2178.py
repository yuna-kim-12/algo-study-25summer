def bfs(maze, N, M):
    from collections import deque
    queue = deque()
    queue.append((0, 0, 1))

    visited = [[0 for _ in range(M)] for _ in range(N)]
    visited[0][0] = 1

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while queue:
        x, y, dist = queue.popleft()

        if x == N - 1 and y == M - 1:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M:
                if maze[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = dist + 1
                    queue.append((nx, ny, dist + 1))

N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, list(input()))))

answer = bfs(maze, N, M)
print(answer)