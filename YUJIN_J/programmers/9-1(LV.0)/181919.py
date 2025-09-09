def solution(n):
    answer = [n]
    while n !=1:
        if n%2==0:
            answer.append(n//2)
            n = n//2
        else:
            answer.append(3*n+1)
            n = 3*n+1      
    return answer