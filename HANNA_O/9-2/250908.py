# SWEA 4839. 이진탐색 (List 2-2)

# 아이디어
# 1. T, P, Pa, Pb 받아오기
# 2. c=int((l+r)/2)로 쪽수 찾기
# 2-1. c보다 찾을 페이지가 작으면 l과 c 사이값 찾기
# 2-2. c보다 찾을 페이지가 크면 c와 r 사이값 찾기
# 3. A가 이기면 A, B가 이기면 B, 비기면 0 출력하기

import sys
sys.stdin = open('./4839_input.txt')

def binary_search_cnt(P, target):
    l, r = 1, P
    cnt = 0
    while l <= r:
        cnt += 1
        c = int((l+r)/2)
        if c == target:
            return cnt
        elif c < target:
            l = c
        else:
            r = c

T = int(input())
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    A_cnt = binary_search_cnt(P, Pa)
    B_cnt = binary_search_cnt(P, Pb)

    if A_cnt < B_cnt:
        result = 'A'
    elif B_cnt < A_cnt:
        result = 'B'
    else:
        result = 0

    print(f'#{tc} {result}')
