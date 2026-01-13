import sys
sys.stdin = open('n.txt')

T = int(input())
arr = [int(input()) for _ in range(T)]
dp = [0] * (T)

if T <= 2:
    print(sum(arr))

else:
    dp[0] = arr[0]
    dp[1] = arr[1] + arr[0]
    for i in range(2, T):
        dp[i] = max(dp[i-3] + arr[i-1] + arr[i], dp[i-2] + arr[i])

    print(dp[-1])