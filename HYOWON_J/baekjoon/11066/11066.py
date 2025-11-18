import sys
sys.stdin = open('n.txt')
# 풀이를 봐도 모르겠는데요 -> DP 너무 어렵다.

T = int(input())

for _ in range(T):
    K = int(input())
    files = [0] + list(map(int, input().split()))  # 1번 인덱스부터 사용

    # 누적합: prefix[i] = 1번 파일부터 i번 파일까지의 합
    prefix = [0] * (K + 1)
    for i in range(1, K + 1):
        prefix[i] = prefix[i - 1] + files[i]

    # dp[i][j] = i번 파일부터 j번 파일까지를 하나로 합치는 최소 비용
    dp = [[0] * (K + 1) for _ in range(K + 1)]

    # 구간 길이 2 ~ K까지 증가시키면서 채움
    for length in range(2, K + 1):        # 길이
        for i in range(1, K - length + 2):
            j = i + length - 1
            dp[i][j] = 10**18             # 충분히 큰 값으로 초기화

            # 중간 분할 위치 k를 모두 시도
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + (prefix[j] - prefix[i - 1])
                if cost < dp[i][j]:
                    dp[i][j] = cost

    print(dp[1][K])