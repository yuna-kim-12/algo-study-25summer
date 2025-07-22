def solution(money):
    answer = []
    num = money // 5500
    change = money - num*5500
    answer.append(num)
    answer.append(change)
    return answer