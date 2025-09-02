# 파리 퇴치 (List 2-1)

# 아이디어
# 1. T, N, M, 격자판 정보 받아오기
# 2. 1부터 N-M+1까지만 격자판 순회하기
# 2-1. 순회하면서 M*M 칸에 있는 숫자 다 더하기
# 2-2. 더한 값이 최대값보다 클 때 최대값 갱신하기
# 3. 순회 종료 후 최대값 출력하기

import sys
sys.stdin = open('./input (1).txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    maxi = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            s = 0
            # for mi in range(M):
            #     for mj in range(M):
            #         s += matrix[i+mi][j+mj]
            for k in range(M):
                s += sum(matrix[i+k][j:j+M])

            if maxi < s:
                maxi = s

    print(f'#{tc} {maxi}')