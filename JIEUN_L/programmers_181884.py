def solution(numbers, n):
    answer = 0
    for i in range(n) :
        if answer <=  n : 
            answer += numbers[i]
        else : break 

    return answer