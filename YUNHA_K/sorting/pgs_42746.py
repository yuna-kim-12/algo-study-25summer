import functools

def compare(a, b):
    if int(a + b) > int(b + a):
        return 1
    elif int(a + b) < int(b + a):
        return -1
    else:
        return 0


def solution(numbers):
    numbers_str = list(map(str, numbers)) # 숫자를 문자열로 변환
    numbers_str.sort(key=functools.cmp_to_key(compare), reverse=True) # 내림차순 정렬
    answer = ''.join(numbers_str)
    if len(answer) == answer.count('0'):
        answer = '0'
    return answer