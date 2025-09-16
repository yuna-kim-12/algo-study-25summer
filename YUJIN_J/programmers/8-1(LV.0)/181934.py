# 조건 문자열
# 문제 설명
'''
문자열에 따라 다음과 같이 두 수의 크기를 비교하려고 합니다.

두 수가 n과 m이라면
">", "=" : n >= m
"<", "=" : n <= m
">", "!" : n > m
"<", "!" : n < m
두 문자열 ineq와 eq가 주어집니다. ineq는 "<"와 ">"중 하나고, eq는 "="와 "!"중 하나입니다. 그리고 두 정수 n과 m이 주어질 때, n과 m이 ineq와 eq의 조건에 맞으면 1을 아니면 0을 return하도록 solution 함수를 완성해주세요.
'''

# 느낀점: 점점 코드가 길어져서 이게 맞나 싶었음. 더 효율적인 방법 존재할 것 같음. 다른 사람 풀이를 보며 배워야할 것 같음

def solution(ineq, eq, n, m):
    if ineq == "<" and eq == "=":
        if n <= m :
            answer = 1
        else:
            answer = 0
    
    elif ineq == "<" and eq == "!":
        if n < m :
            answer = 1
        else:
            answer = 0
            
    if ineq == ">" and eq == "=":
        if n >= m :
            answer = 1
        else:
            answer = 0
            
    if ineq == ">" and eq == "!":
        if n > m :
            answer = 1
        else:
            answer = 0
    return answer