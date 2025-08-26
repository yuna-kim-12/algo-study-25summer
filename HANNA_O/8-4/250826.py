# baby-gin 실습 (List 1-2)

# 아이디어
# 1. T, 숫자카드 받기
# 2. 0-9까지 카드 개수를 셀 수 있는 리스트 만들기
# 3. baby-gin인지 확인할 수 있는 카운트 변수 만들기
# 4. 리스트를 순회하며 카드가 3개 이상인 숫자 찾기(triplet 찾기)
# 4-1. 만약 있다면 -3하고 카운트 +1 또는 -6하고 카운트 +2
# 5. 카운트가 1이라면 리스트 다시 순회해서 카드가 1개 이상인 것 찾기
# 5-1. 카드가 2개 이상이면 멈추고 false 출력
# 5-2. 카드가 1개 이상이면 그 다음 수, 그 다다음 수도 1개 이상인지 알아보고 맞다면 카운트 +1
# 6. 카운트가 2라면 true 출력, 아니라면 false 출력

import sys
sys.stdin = open('./input (1).txt')

T = int(input())
for tc in range(1, T+1):
    nums = input()
    nums_cnt = [0] * 10
    cnt = 0

    for n in nums:
        nums_cnt[int(n)] += 1

    for i in range(10):
        while nums_cnt[i] >= 3:
            nums_cnt[i] -= 3
            cnt += 1

    for i in range(8):
        while nums_cnt[i] >= 1 and nums_cnt[i+1] >= 1 and nums_cnt[i+2] >= 1:
            nums_cnt[i] -= 1
            nums_cnt[i+1] -= 1
            nums_cnt[i+2] -= 1
            cnt += 1

    if cnt == 2:
        print(f'#{tc} true')
    else:
        print(f'#{tc} false')