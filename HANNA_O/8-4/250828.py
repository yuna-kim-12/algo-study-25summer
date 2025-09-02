# 풍선팡2 (List2-1)

# 아이디어
# 1. T, N, M, 꽃가루 정보 격자판 받아오기
# 2. 격자판을 순회화며 자신, 상, 하, 좌, 우 보면서 터지는 꽃가루 개수 세기
# 2-1. 상하좌우 존재여부 확인 필수
# 3. 만약 현재 값이 최대라면 최대값 갱신하기
# 4. 순회를 마친 후 최대값 출력하기

import sys
sys.stdin = open('./input1.txt')

direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    maxi = 0

    for i in range(N):
        for j in range(M):
            cnt = matrix[i][j]

            for r, c in direc:
                if 0 <= i+r < N and 0 <= j+c < M:
                    cnt += matrix[i+r][j+c]

            if cnt > maxi:
                maxi = cnt

    print(f'#{tc} {maxi}')