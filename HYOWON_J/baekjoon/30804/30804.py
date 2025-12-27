import sys
from collections import deque
sys.stdin = open('n.txt')

# 딕셔너리 + 덱 풀이 -> 시간초과
# N = int(input())
# q = deque(map(int, input().split()))
# dict_q = {}
# for i in range(N):
#     if q[i] not in dict_q:
#         dict_q[q[i]] = 1
#         continue
#     dict_q[q[i]] += 1
#
# while len(set(q)) > 2:
#     a = q.popleft()
#     b = q.pop()
#     if dict_q[a] > dict_q[b]:
#         q.appendleft(a)
#     else:
#         q.append(b)
#
# print(len(q))

N = int(input())
arr = list(map(int, input().split()))

cnt = {}
left = 0
distinct = 0
ans = 0

for right, x in enumerate(arr):
    if cnt.get(x,0) == 0:
        distinct += 1
    cnt[x] = cnt.get(x, 0) + 1

    while distinct > 2:
        y = arr[left]
        cnt[y] -= 1
        if cnt[y] == 0:
            distinct -=1
            del cnt[y]
        left += 1

    ans = max(ans, right - left + 1)

print(ans)