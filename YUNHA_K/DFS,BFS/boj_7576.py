import sys
input = sys.stdin.readline

# dirs울 활용해서 인접해 있는 토마토를 익히자. 상하좌우만 익히면 됨.
dirs = ((-1,0),(1,0),(0,-1),(0,1))
def new_bfs(tomatoes):
    from collections import deque
    queue = deque([])

    for i in range(N):
        for j in range(M):
            if tomatoes[i][j] == 1:
                queue.append((i,j,0))

    result = 0
    while queue:
        ci, cj, day = queue.popleft()
        for di in dirs:
            ni, nj = ci + di[0], cj + di[1]
            if 0 <= ni < N and 0 <= nj <M and tomatoes[ni][nj] == 0:
                tomatoes[ni][nj] = 1
                queue.append((ni,nj,day+1))
        result = day

    for lst in tomatoes:
        for tomato in lst:
            if tomato == 0:
                return -1
    return result

# 입력 : 익은 토마토 1, 안익은 토마토 0, 토마토 없음 -1
M, N = map(int, input().split())
tomatoes = []
for _ in range(N):
    tomatoes.append(list(map(int, input().split())))

print(new_bfs(tomatoes))