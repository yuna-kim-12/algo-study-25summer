# 배열 만들기 2

def solution(l, r):
    answer = []

    def dfs(num):
        if num > r:
            return
        if num >= l:
            answer.append(num)
        dfs(num * 10 + 0)
        dfs(num * 10 + 5)

    dfs(5)  # 첫 자리 숫자는 5로 시작

    if not answer:
        return [-1]
    return sorted(answer)