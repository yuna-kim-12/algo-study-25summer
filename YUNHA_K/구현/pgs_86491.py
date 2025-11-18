# 풀이 : 왼쪽에 큰 거 위치시키고, 각 인덱스의 최대 값 곱한 값 리턴
def solution(sizes):
    max_left = 0
    max_right = 0
    for x in sizes:
        if x[0] < x[1]:
            x[0], x[1] = x[1], x[0]
        if x[0] > max_left:
            max_left = x[0]
        if x[1] > max_right:
            max_right = x[1]
        
    answer = max_left * max_right
    return answer
