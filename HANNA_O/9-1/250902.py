# SWEA 1979. 어디에 단어가 들어갈 수 있을까? (List 2-1)

# 아이디어
# 1. T, N, K, 퍼즐 정보 받아오기
# 2. 퍼즐을 순회하면서 가로, 세로에 들어갈 수 있는 자리가 있는지 확인하기
# 2-1. 1이 나오면 카운트하기
# 2-2. 0이 나오거나 마지막 자리에 갔을때 카운트가 K와 같다면 가능한 자리수 +1 아니라면 지나가기
# 3. 한 줄씩 반복
# 4. 가능한 자리수 출력하기

import sys
sys.stdin = open('./input (1).txt')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    w, h = 0, 0

    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1:
                w += 1

            if puzzle[j][i] == 1:
                h += 1

            if puzzle[i][j] == 0 or j == N-1:
                if w == K:
                    answer += 1
                w = 0

            if puzzle[j][i] == 0 or j == N-1:
                if h == K:
                    answer += 1
                h = 0

    print(f'#{tc} {answer}')

    # 위에 코드에서 `if puzzle[j][i] == 0 or j == N-1:` 이 부분을 `if puzzle[j][i] == 0 or i == N-1:`로 해서 답이 나오지 않음
    # 즉, 세로줄의 끝 확인하는 코드 잘못되어 있었음.
    # 아래는 gemini 참고 코드
    # # 가로탐색
    # for i in range(N):
    #     cnt = 0
    #     for j in range(N):
    #         if puzzle[i][j] == 1:
    #             cnt += 1
    #         else:
    #             if cnt == K:
    #                 answer += 1
    #             cnt = 0
    #
    #     if cnt == K:
    #         answer += 1
    #
    # # 세로 탐색
    # for j in range(N):
    #     cnt = 0
    #     for i in range(N):
    #         if puzzle[i][j] == 1:
    #             cnt += 1
    #         else:
    #             if cnt == K:
    #                 answer += 1
    #             cnt = 0
    #
    #     if cnt == K:
    #         answer += 1
    #
    # print(f'#{tc} {answer}')