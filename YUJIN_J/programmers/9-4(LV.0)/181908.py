# 배열 만들기5

def solution(intStrs, k, s, l):
    answer = []
    t = 0
    for i in intStrs:
        t = i[s:s+l]
        if int(t) > k:
            answer.append(int(t))
    return answer