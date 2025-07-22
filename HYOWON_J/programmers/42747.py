def solution(citations):
    answer = 0

    citations.sort(reverse=True)

    #h 최솟값이라 생각하고 찾으면
    for i in range(len(citations)):
        if (i + 1) <= citations[i]:
            answer = i + 1

    return answer


print(solution([4, 1, 2, 1, 5]))#2
print(solution([3, 0, 6, 1, 5]))#3