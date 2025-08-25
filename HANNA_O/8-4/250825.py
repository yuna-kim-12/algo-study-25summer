# 삼성시의 버스 노선 (List 1-2)

# 아이디어
# 1. T, N, 두 정수 A, B, P, Plist 받아오기
# 2. Plist 안의 숫자들이 A-B 안에 포함이 되는지 확인하기
# 2-1. 만약 포함이 된다면 해당 인덱스에 +1하기

import sys
sys.stdin = open('./s_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ab = []
    for n in range(N):
        ab.append(list(map(int, input().split())))

    P = int(input())
    Plist = [int(input()) for _ in range(P)]
    lst = [0] * P

    for i in range(P):
        for a, b in ab:
            if a <= Plist[i] <= b:
                lst[i] += 1

    print(f'#{tc}', *lst)