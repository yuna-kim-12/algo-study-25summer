# SWEA 1974. 스도쿠 검증 (List 2-1)

# 아이디어
# 1. T, 스토쿠 받아오기
# 2. 가로, 세로, 정사각형에 1-9까지의 숫자가 모두 들어있는지 확인하기
# 2-1. 1-9까지 체크할 수 있는 리스트 만들고 0이 있는지 확인(0이 있으면 1-9 중 없는 숫자 있다는 증거)
# 2-2. 0이 있을 경우 바로 검증 멈추고 0 출력
# 2-3. 0이 없다면 1 출력

import sys
sys.stdin = open('./input (1).txt')

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    answer = 1

    for i in range(9):
        w = [0] * 9
        h = [0] * 9

        for j in range(9):
            w[sudoku[i][j]-1] += 1
            h[sudoku[j][i]-1] += 1

            if i in [0, 3, 6] and j in [0, 3, 6]:
                s = [0] * 9
                for si in range(i, i+3):
                    for sj in range(j, j+3):
                        s[sudoku[si][sj]-1] += 1

                if 0 in s:
                    answer = 0
                    break

        if 0 in w or 0 in h or answer == 0:
            answer = 0
            break

    print(f'#{tc} {answer}')