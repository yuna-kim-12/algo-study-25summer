# SWEA 1209. Sum (List 2-1)

# 아이디어
# 1. tc 번호, 배열 정보 받아오기
# 2. 배열을 순회 하면서 합이 최대값 보다 크다면 갱신하기
# 2-1. 가로는 [i][j]로 세로는 [j][i]로 정방향 대각선은 i=j일 때, 역방향 대각선은 i=100-j일때로 구하기
# 3. 최대값 출력하기

import sys
sys.stdin = open('./input (1).txt')

for _ in range(10):
    tc = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    maxi = 0
    w, h, d, rd = 0, 0, 0, 0

    for i in range(100):
        for j in range(100):
            w += matrix[i][j]
            h += matrix[j][i]

            if i == j:
                d += matrix[i][j]

            if i == 100 - j:
                rd = matrix[i][j]

        if maxi < w:
            maxi = w
        if maxi < h:
            maxi = h
        w, h = 0, 0

    if maxi < d:
        maxi = d
    if maxi < rd:
        maxi = rd

    print(f'#{tc} {maxi}')
