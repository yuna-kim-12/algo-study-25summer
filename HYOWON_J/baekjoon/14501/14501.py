import sys
sys.stdin = open('num.txt')

N = int(input())
schedule = [[0,0] for _ in range(N+1)]
for i in range(1, N+1):
    T, P = map(int, input().split())
    schedule[i][0] = T
    schedule[i][1] = P

dp = [0] * (N+2)

for i in range(N, 0, -1):
    if schedule[i][0] + i > N + 1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], schedule[i][1] + dp[i + schedule[i][0]])

print(dp[1])