# SWEA 1954. 달팽이 숫자 (List 2-2)

# 아이디어
# 1. T, N 받아오기
# 2. 달팽이 숫자 채워넣을 2차원 배열 만들기
# 3. 행, 열, 방향, 숫자 변수 만들기
# 3-1. 방향 : 0 오른쪽, 1 아래, 2 왼쪽, 3 위
# 4. N * N만큼 반복하며 배열에 숫자 채우기
# 4-1. 숫자 채우고 num += 1
# 4-2. 만약 배열 범위 벗어나거나 이미 숫자 채워져 있으면 방향 전환하기
# 4-3. 다음 숫자 채울 행, 열 갱신
# 5. 달팽이 숫자 출력하기


import sys
sys.stdin = open('./input (1).txt')

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    x, y = 0, 0
    dire = 0
    num = 1

    for _ in range(N*N):
        arr[x][y] = num
        num += 1

        nx = x + dx[dire]
        ny = y + dy[dire]

        if not (0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0):
            dire = (dire + 1) % 4
            nx = x + dx[dire]
            ny = y + dy[dire]

        x, y = nx, ny

    print(f'#{N}')
    for r in arr:
        print(' '.join(map(str, r)))