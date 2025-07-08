def solution(arr, k):
    answer = []

    for i in arr:
        if i not in answer and len(answer) != k:
            answer.append(i)

    len_answer = len(answer)
    if len_answer != k:
        re = k - len_answer
        for _ in range(re):
            answer.append(-1)

    return answer

print(solution([0, 1, 1, 2, 2, 3], 3))
print(solution([0, 1, 1, 1, 1], 4))