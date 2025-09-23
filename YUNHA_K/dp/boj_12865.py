import sys
input = sys.stdin.readline

def get_max_value():
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(1,N+1):
        w, v = products[i][0], products[i][1]
        for j in range(1,K+1):
            if w > j:
                dp[i][j] = dp[i-1][j]
            else:
                productout = dp[i-1][j]
                productin = dp[i-1][j-w] + v
                dp[i][j] = max(productin, productout)

    return dp[N][K]

# 입력
N, K = map(int, input().strip().split())
products = [(0,0)]

for i in range(N):
    W, V = map(int, input().strip().split())
    products.append((W,V))

print(get_max_value())