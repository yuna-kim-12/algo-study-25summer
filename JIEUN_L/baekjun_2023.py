import sys 

sys.stdin = open("input.txt")

"""
이건 절대 에라토스테네스의 체로는 풀 수 없는 문제이다. 메모리 제한이 걸렸기 때문이당... 이 문제는 DFS문제이다..... ㅠㅠㅠㅠ

1. 10까지의 소수를 모두 적어놓는다. 
2. 첫 자리는 2부터 해도 된다. 2나 홀수인지 확인한다.
3. 조건을 만족하면, 그 뒷자리에 홀수를 붙인다. 그러고 find_prime을 돌린다. True라면 이후 계속 숫자를 붙인다.
4. 자릿수에 도달할 때 까지 한다,
"""

import math

answer = []

def find_prime(number) :
    div =  int(math.sqrt(number)//1) 
    for i in range(3, div+1) : # 2 는 어차피 소수니까 버리셈.
        if number%i == 0 :
            return False
    return True
        
def DFS(number, idx, answer, N) : 
    
    if not idx ==1 and not find_prime(number) : 
        return 
    if idx == N : 
        answer.append(number)
        return answer
    
    for o in (1, 3, 5, 7, 9) : 
        DFS(number*10 + o,idx+1, answer, N)
    
    return answer



N = int(input())

min_num = int('9'*N)
max_num = int('1'+'0'*(N-1))
answer = []
for num in [2, 3, 5, 7] :
    answer.extend(DFS(num, 1, [], N))

answer.sort()
for i in range(len(answer)) : 
    print(answer[i])
