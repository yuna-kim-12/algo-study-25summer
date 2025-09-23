# SWEA 9490. 풍선팡 (List 2-2)

# 아이디어
# 1. T, N, M, 꽃가루 배열 정보 받아오기
# 2. 배열을 순회하면서 현재 꽃가루 개수만큼 상, 하, 좌, 우에 들어있는 풍선 터트리기
# 2-1. 각 풍선의 꽃가루 개수의 총합 구하기
# 3. 총합이 최대값보다 크다면 갱신하기
# 4. 배열 순회를 마친 후 최대값 출력하기

import sys
sys.stdin = open('input1.txt')

d = [(-1, 0), (0, 1), (1, 0), (0, -1)]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    maxi = 0

    for i in range(N):
        for j in range(M):
            total = matrix[i][j]

            for idx in range(1, matrix[i][j]+1):
                for c, r in d:
                    ni = i + c*idx
                    nj = j + r*idx
                    if 0 <= ni < N and 0 <= nj < M:
                        total += matrix[ni][nj]

            if maxi < total:
                maxi = total
                total = 0

    print(f'#{tc} {maxi}')