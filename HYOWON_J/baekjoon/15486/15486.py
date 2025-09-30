import sys
sys.stdin = open('n.txt')

N = int(input())
work = [list(map(int, input().split())) for _ in range(N)]
dp = [0] * (N+1)
max_in = 0
max_check = [0] * (N+1)

# max_in = 현재 얻을 수 있는 최댓값
for i in range(N):
    max_in = max(max_in, dp[i])
    max_check[i] = max_in
    if work[i][0] + i > N:
        continue

    dp[i + work[i][0]] = max(max_in + work[i][1], dp[i + work[i][0]])

print(max(dp))
print(dp)
print(max_check)