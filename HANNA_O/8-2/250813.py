# Flatten (List 1-2)

# 아이디어
# 1. 덤프 횟수, 상자 높이 리스트 받아오기
# 2. 상자 높이 리스트에서 최대값과 최소값 가져오기(min, max 사용)
# 3. 최대값 -1, 최소값 +1 하기(min, max의 index 알아야함)
# 4. 2-3번 덤프 횟수만큼 반복
# 4-1. 만약 덤프 횟수 안에 평탄화가 끝나면(최대값과 최소값의 차이가 1 이하면) 멈추기
# 5. 최대값 - 최소값 출력하기

import sys
sys.stdin = open('./input (1).txt')

# min, max, index 사용 -> 시간복잡도 높음
# T = 10
# for tc in range(1, T+1):
#     cnt = int(input())
#     boxes = list(map(int, input().split()))
#
#     for n in range(cnt):
#         if max(boxs) - min(boxs) <= 1:
#             break
#
#         max_idx = boxs.index(max(boxs))
#         min_idx = boxs.index(min(boxs))
#         boxs[max_idx] -= 1
#         boxs[min_idx] += 1
#
#     print(f'#{tc} {max(boxs) - min(boxs)}')


# 정렬 사용 -> 시간복잡도 낮음
T = 10
for tc in range(1, T+1):
    cnt = int(input())
    boxes = list(map(int, input().split()))

    for _ in range(cnt):
        boxes.sort()

        if boxes[-1] - boxes[0] <= 1:
            break

        boxes[-1] -= 1
        boxes[0] += 1

    boxes.sort()

    print(f'#{tc} {boxes[-1] - boxes[0]}')