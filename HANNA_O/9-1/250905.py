# SWEA 1961. 숫자 배열 회전 (List 2-2)

# 아이디어
# 1. T, N, 헹렬 정보 받아오기
# 2. 90, 180, 270 도로 돌린 행렬 출력하기
# 2-1. 행, 열 순환 N -> 0으로 거꾸로 순환
# 2-2. 한 줄 씩 출력하기 위해 문자열 더할 배열 만들기
# 2-3. 열 순환 시 [j][N-1-i], [i][j], [N-1-j][i]
# 2-4. 행 순환 시 출력하기(줄 바꾸기

import sys
sys.stdin = open('./input (1).txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(str, input().split())) for _ in range(N)]

    print(f'#{tc}')

    for i in range(N-1, -1, -1):
        answer = [''] * 3
        for j in range(N-1, -1, -1):
            answer[0] += matrix[j][N-1-i]
            answer[1] += matrix[i][j]
            answer[2] += matrix[N-1-j][i]

        print(*answer)