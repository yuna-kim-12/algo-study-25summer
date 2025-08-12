# 숫자 카드 (List 1-2)

# 아이디어
# 1. T, N, 숫자 리스트 받아오기
# 2. 0-9가 적힌 카드 개수를 셀 수 있는 리스트 만들기
# 3. 숫자 리스트 순회하며 카드 세기
# 4. 카드 개수 리스트 역순회하며 최대 개수와 숫자 찾기
    # - 역순으로 하는 이유 : 카드 개수가 같을 때 더 큰 숫자 뽑기 위해


import sys
sys.stdin = open('./sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = input()
    counts = [0] * 10

    for n in nums:
        counts[int(n)] += 1

    max_cnt = 0
    max_num = 0

    for i in range(9, -1, -1):
        if counts[i] > max_cnt:
            max_cnt = counts[i]
            max_num = i

    print(f'#{tc} {max_num} {max_cnt}')