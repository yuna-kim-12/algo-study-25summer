# 간단한 소인수분해 (List 1-2)

# 아이디어
# 1. T, N 받아오기
# 2. N을 2, 3, 5, 7, 11 순으로 나누기
# 2-1. 그 수로 나눌 수 있을 때 나누고, 카운트 +1
# 2-2. 그 수로 더이상 나눌 수 없을 때 다음 수로 넘어가기
# 3. 각 수마다 나눈 횟수 출력하기

import sys
sys.stdin = open('./input (1).txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    primes = [2, 3, 5, 7, 11]
    cnts = [0] * 5

    for i in range(5):
        while N % primes[i] == 0:
            N //= primes[i]
            cnts[i] += 1

    print(f'#{tc}', *cnts)