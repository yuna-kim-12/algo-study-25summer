def solution(brown, yellow):
    answer = []
    num_1 = 3
    total = brown + yellow

    while True:
        if total % num_1 == 0:
            num_2 = total//num_1
            if (num_1 * 2) + (num_2 - 2) * 2 == brown:
                answer.append(num_2)
                answer.append(num_1)
                break
            else:
                num_1 += 1
        else:
            num_1 += 1

    answer.sort(reverse=True)

    return answer


print(solution(10, 2))
print(solution(8,1))
print(solution(24,24))