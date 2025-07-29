def solution(quiz):
    answer = []
    for q in quiz:
        parts = q.split()
        num1 = int(parts[0])
        operator = parts[1]
        num2 = int(parts[2])
        result = int(parts[4])

        if operator == '+':
            if num1 + num2 == result:
                answer.append("O")
            else:
                answer.append("X")
        else:
            if num1 - num2 == result:
                answer.append("O")
            else:
                answer.append("X")

    return answer