# 1.일단 숫자 7개를 가지고 permutation 을 해본다. 

# def solution(numbers):
#     answer = 0
#     return answer

from itertools import permutations
import math

def find_prime(val) : 
    for i in range(2, int(math.sqrt(val))) :
        if val%i == 0 : 
            return False
    return True

def solution(numbers):
    answer =0 
    perm = []
    perm_set = set([])
    for i in range(1, len(numbers)+1) : 
        perm = perm+list(permutations(numbers, i))
    for i in range(len(perm)) : 
        if perm[i][-1] not in ["0,  4, 6, 8"]  : 
            temp  =""
            for p in perm[i] : 
                temp += p    
            perm_set.add(int(temp))
    # print(perm_set)
    for p in perm_set : 
        if p > 1 and find_prime(p) : 
            answer += 1


    return answer


print(solution("111"))