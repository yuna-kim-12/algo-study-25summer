import sys
input = sys.stdin.readline

from collections import Counter

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
result_nums = list(map(int, input().split()))

num_counts = Counter(nums)

for num in result_nums:
    if num in num_counts.keys():
        print(num_counts[num], end=" ")
    else:
        print(0, end=" ")