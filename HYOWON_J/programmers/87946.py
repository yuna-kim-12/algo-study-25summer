def solution(number, k):
    answer = ''
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)

    #k가 남아 있을 경우
    if k:
        for s in range(len(stack) - k):
            answer += stack[s]
    #k가 없을 경우
    else:
        for s in stack:
            answer += s

    return answer


print(solution("1924", 2))
print(solution("1231234",3))
print(solution("4177252841",4))