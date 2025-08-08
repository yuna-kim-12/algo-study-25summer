def solution(name):
    answer = 0
    A = 65
    Z = 90
    for i in name:
        answer += min(ord(i) - A,  Z - ord(i) + 1)

    n = len(name)
    move = n-1

    for now in range(n):
        next = now + 1
        while next < n and name[next] == "A":
            next += 1
        move = min(move, now + n - next + min(now, n - next))

    answer += move

    return answer

print(solution("JEROEN"))
print(solution("JAN"))
print(solution("JAZAA"))