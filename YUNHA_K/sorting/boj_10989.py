import sys
input = sys.stdin.readline

N = int(input())
lst = [0]*10001
for _ in range(N):
    num = int(input())
    lst[num] += 1

for i in range(10001):
    if lst[i]:
        for _ in range(lst[i]):
            print(i)

