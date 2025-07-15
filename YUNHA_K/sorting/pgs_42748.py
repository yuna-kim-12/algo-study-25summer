def solution(array, commands):
    answer = []

    for lst in commands:
        start, last, n = lst
        ar_lst = sorted(array[start - 1:last])
        answer.append(ar_lst[n - 1])

    return answer