# def solution(k, dungeons):
#     answer = 0
#
#     sorted_dungeons = sorted(dungeons, key=lambda x:(x[0]-x[1], -x[0]), reverse=True)
#     print(sorted_dungeons)
#     for dungeon in sorted_dungeons:
#         if k >= dungeon[0]:
#             k -= dungeon[1]
#             answer += 1
#
#     if answer:
#         return answer
#     else:
#         return -1

from itertools import permutations

def solution(k, dungeons):
    max_cnt = 0
    for order in permutations(dungeons, len(dungeons)):
        tired = k
        cnt = 0
        for minimum, cost in order:
            if tired >= minimum:
                tired -= cost
                cnt += 1
            else:
                break
        max_cnt = max(max_cnt, cnt)
    return max_cnt

print(solution(80,[[80, 80], [50, 30], [30, 10]]))