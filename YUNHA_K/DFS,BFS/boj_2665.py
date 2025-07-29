from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, list(input().strip()))))

# (r, c)까지 도달하는 데 필요한 최소 검은 방 변경 횟수 (비용)
# 충분히 큰 값으로 초기화 (무한대)
INF = int(1e9)
dist = [[INF] * N for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque()

# 시작점 (0,0) 초기화
dist[0][0] = 0
q.appendleft((0, 0)) # 비용이 0이므로 덱의 앞에 삽입

while q:
    r, c = q.popleft()

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if not (0 <= nr < N and 0 <= nc < N):
            continue

        # 다음 칸이 흰 방 (비용 0)
        if board[nr][nc] == 1:
            # 현재 경로의 비용이 더 작다면 업데이트
            if dist[r][c] < dist[nr][nc]:
                dist[nr][nc] = dist[r][c]
                q.appendleft((nr, nc)) # 비용 0이므로 덱의 앞에 삽입 (우선 탐색)
        # 다음 칸이 검은 방 (비용 1)
        else: # board[nr][nc] == 0
            # 현재 경로의 비용 + 1 (검은 방을 바꾸는 비용)이 더 작다면 업데이트
            if dist[r][c] + 1 < dist[nr][nc]:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc)) # 비용 1이므로 덱의 뒤에 삽입 (나중에 탐색)

# 도착점 (N-1, N-1)까지의 최소 비용 출력
print(dist[N-1][N-1])