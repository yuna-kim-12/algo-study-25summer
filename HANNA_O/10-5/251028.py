# programmers 삼총사 (조합)

# 아이디어
# 1. 반복문으로 세 수의 조합 찾기
# 2. 각 자리의 범위 : i(0 ~ n-3), j(i+1 ~ n-2), k(j+1 ~ n-1)
# 3. 조합한 세 수의 합이 0인지 확인하기
# 4. 0이 맞다면 cnt +1
# 5. cnt 출력하기

def solution(num):

    cnt = 0
    n = len(num)

    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if num[i] + num[j] + num[k] == 0:
                    cnt += 1

    return cnt