import sys
sys.stdin = open("num.txt")

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)
answer = 0

for coin in coins:
    if coin <= K:
        while K - coin >= 0:
            answer += 1
            K = K - coin

print(answer)