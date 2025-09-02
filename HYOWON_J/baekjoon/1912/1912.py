import sys
sys.stdin = open("1912.txt")

n = int(input())
num = list(map(int, input().split()))

now_max = num[0]
global_max = num[0]

for i in range(1, n):
    print(now_max, num[i], now_max + num[i])
    now_max = max(num[i], now_max+num[i])
    if now_max > global_max:
        global_max = now_max

print(global_max)