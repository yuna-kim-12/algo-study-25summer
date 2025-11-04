# programmers 최소 직사각형 (완전탐색)

# 아이디어
# 1. 각 명함의 큰 길이를 앞에, 작은 길이를 뒤에 배치하기
# 2. 만약 배치된 앞에 값이 기존 값보다 크면 갱신하기
# 2-1. 뒤도 마찬가지로 기존 값보다 크면 갱신하기
# 3. 갱신된 앞, 뒤 값 곱해서 출력하기


def solution(sizes):
    # 최소값, 최대값이 잘못 정의 되어서 틀림(무조건 첫번째 값이 작을 수 없음)
    # max_l, max_s = sizes[0][0], sizes[0][1]
    # 초기값을 0으로 설정해 모든 명함의 값과 비교할 수 있도록 수정
    max_l, max_s = 0, 0

    for size in sizes:
        long = max(size)
        short = min(size)

        if long > max_l:
            max_l = long

        if short > max_s:
            max_s = short

    answer = max_l * max_s
    return answer

