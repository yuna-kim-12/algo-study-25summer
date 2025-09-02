from collections import defaultdict
import sys

input = sys.stdin.readline

dictionary = defaultdict(set)

N = int(input())
for _ in range(N):
    val = input().strip()
    dictionary[len(val)].add(val)

lens = sorted(list(dictionary.keys()))


for i in lens:
    lst = list(dictionary[i])
    for val in sorted(lst):
        print(val)

# ==============최적화 풀이===================
# dictionary = set()
#
# N = int(input())
# for _ in range(N):
#     dictionary.add(input().strip())
#
# for word in sorted(dictionary, key=lambda x: (len(x), x)):
#     print(word)