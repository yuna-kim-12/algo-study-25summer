def solution(m, n, puddles):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in puddles:
        dp[i[1]][i[0]] = -1

    dp[1][1] = 1
    print(dp)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue

            if i > 1:
                dp[i][j] += dp[i - 1][j]
            if j > 1:
                dp[i][j] += dp[i][j - 1]

    return dp[n][m] % 1000000007

print(solution(4,3,[[2, 2]]))