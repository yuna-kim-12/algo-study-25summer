import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
n_nums = list(map(int, input().split()))
M = int(input())
m_nums = list(map(int, input().split()))

n_counts = Counter(n_nums)
for num in m_nums:
    if n_counts[num]:
        print(1)
    else:
        print(0)
