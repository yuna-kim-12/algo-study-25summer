# 접미사 배열

def solution(my_string):
    answer = []
    for i in range(0, len(my_string)):
        answer.append(my_string[i:])
    return sorted(answer)