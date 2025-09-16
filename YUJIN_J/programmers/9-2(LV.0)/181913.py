# 문자열 여러 번 뒤집기

def solution(my_string, queries):
    answer=''
    for s, e in queries:
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    answer = my_string
    return answer