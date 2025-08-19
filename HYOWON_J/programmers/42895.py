def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]
    dp[1].add(N)

    for i in range(2, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i - j]:
                    dp[i].add(x + y)
                    dp[i].add(x - y)
                    dp[i].add(x * y)
                    if y != 0:
                        dp[i].add(x // y)

        if number in dp[i]:
            return i

    return -1

print(solution(5, 12))