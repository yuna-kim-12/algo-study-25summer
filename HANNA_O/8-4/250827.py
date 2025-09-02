# 색칠하기 (List 2-1)

# 아이디어
# 1. T, N 받아오기
# 2. 10 * 10 격자판 만들기
# 3. 칠할 영역의 정보 받아오면서 격자판 칠하기
# 3-1. 현재 칠하려는 영역이 0이라면 현재 칠하려는 영역 표시
# 3-2. 칠하려는 영역과 이미 적혀있는 영역이 다르다면 3(보라)로 바꾸고 카운트 +1


import sys
sys.stdin = open('./4836_sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [[0] * 10 for _ in range(10)]
    cnt = 0

    for i in range(N):
        spot = list(map(int, input().split()))

        for r in range(spot[0], spot[2]+1):
            for c in range(spot[1], spot[3]+1):
                if matrix[r][c] == 0:
                    matrix[r][c] = spot[4]
                elif matrix[r][c] == 3:
                    continue
                elif spot[4] != matrix[r][c]:
                    matrix[r][c] = 3
                    cnt += 1

    print(f'#{tc} {cnt}')