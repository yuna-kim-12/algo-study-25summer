import sys
sys.stdin = open('num.txt')

# N, M = map(int, input().split())
# T = set(input().split()[1:])
# party = []
#
# for _ in range(M):
#     party.append(set(input().split()[1:]))
#
# for _ in range(M):
#     for p in party:
#         if p & T:
#             T = T.union(p)
#
# cnt = 0
# for i in party:
#     if i & T:
#         continue
#     cnt += 1
#
# print(cnt)

