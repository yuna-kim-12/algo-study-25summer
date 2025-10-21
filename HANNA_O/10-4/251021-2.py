# programmers 콜라츠 추측

# 아이디어
# 1. 반복 횟수 제한하기(n이 1이 되기까지 최대 500번만 반복)
# 2. 콜라츠 과정 구현하기
# 2-1. n이 짝수면 2로 나누기
# 2-2. n이 홀수면 3곱하고 1 더하기
# 2-3. n이 1이 될 때까지 위 과정 반복
# 3. 반복 횟수가 500번을 넘을 경우 -1 반환 아니라면 반복 횟수 반환

def solution(n):
    if n == 1:
        return 0

    count = 0

    for count in range(500):
        # 짝수 처리
        if n % 2 == 0:
            n = n // 2

        # 홀수 처리
        else:
            n = (n * 3) + 1

        if n == 1:
            return count + 1

    return -1