# SWEA 1210. Ladder1 (List2-2)

# 아이디어
# 1. 테스트 번호, 사다리표 정보 가져오기
# 2. 맨 아래줄에서 2인 위치 찾기
# 3. 한칸씩 위로 올라가다가(윗 칸이 1인 경우) 왼쪽 또는 오른쪽에 1이 나타난다면 방향 틀기
# 3-1. 한 칸씩 그 방향으로 가다가 끊기면 위로 올라가기
# 3-2. 맨 윗줄에 도착할 때까지 반복
# 4. 맨 윗줄에 도착한 위치 출력하기

import sys
sys.stadin = open('./input (1).txt')

for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    x = ladder[99].index(2)
    y = 99

    while y > 0:
        if x > 0 and ladder[y][x-1] == 1:
            while x > 0 and ladder[y][x-1] == 1:
                x -= 1

        elif x < 99 and ladder[y][x+1] == 1:
            while x < 99 and ladder[y][x+1] == 1:
                x += 1

        y -= 1

    print(f'#{tc} {x}')
