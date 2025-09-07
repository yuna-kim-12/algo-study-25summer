import sys
input = sys.stdin.readline

# 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 여섯 방향 토마토
dirs = ((1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,-1),(0,0,1))

def first_location(tomatoes:list):
    queue = []
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] == 1:
                    queue.append((i,j,k,0))
    return queue

def check_box(tomatoes:list):
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatoes[i][j][k] == 0:
                    return 1
    return 0

def bfs(tomatoes:list):
    from collections import deque
    queue = deque(first_location(tomatoes))

    while queue:
        ci, cj, ck, result = queue.popleft()

        for dir in dirs:
            ni, nj, nk = ci+dir[0], cj+dir[1], ck+dir[2]
            if 0<= ni < H and 0 <= nj < N and 0 <= nk < M and tomatoes[ni][nj][nk] == 0:
                tomatoes[ni][nj][nk] = 1
                queue.append((ni,nj,nk,result+1))

    if check_box(tomatoes):
        return -1
    return result

# 입력
# M, N, H 가로, 세로, 높이
M, N, H = map(int, input().split())
tomatoes = []
for _ in range(H):
    layer = []
    for _ in range(N):
        layer.append(list(map(int, input().split())))
    tomatoes.append(layer)

if not check_box(tomatoes):
    print(0)
else:
    print(bfs(tomatoes))


# def solve():
#     from collections import deque
#     M, N, H = map(int, input().split())
#     tomatoes = []
#     queue = deque()
#     unriped_count = 0
#
#     for i in range(H):
#         layer = []
#         for j in range(N):
#             row = list(map(int, input().split()))
#             layer.append(row)
#             for k in range(M):
#                 if row[k] == 1:
#                     queue.append((i,j,k,0))
#                 elif row[k] == 0:
#                     unriped_count += 1
#         tomatoes.append(layer)
#
#     if unriped_count == 0:
#         return 0
#
#     while queue:
#         ci, cj, ck, result = queue.popleft()
#
#         for dir in dirs:
#             ni, nj, nk = ci + dir[0], cj + dir[1], ck + dir[2]
#             if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and tomatoes[ni][nj][nk] == 0:
#                 tomatoes[ni][nj][nk] = 1
#                 unriped_count -= 1
#                 queue.append((ni, nj, nk, result + 1))
#
#     return result if unriped_count == 0 else -1
#
# print(solve())