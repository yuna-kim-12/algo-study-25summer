# programmers 기능개발 (스택, 큐)

# 아이디어
# 1. 진도율과 개발 속도로 각 작업이 걸리는 일수 구하기
# 2. 현재 작업이 걸리는 속도보다 뒤에 있는 작업 속도가 더 빠르다면 카운트 +1
# 2-1. 뒤에 있는 게 더 느리다면 현재 카운트 answer 배열에 집어 넣기
# 2-2. 그 후 그 다음 것부터 카운트 다시 세기
# 2-3. 배열 끝까지 위 과정 반복

def solution(progresses, speeds):
    answer = []
    days = []

    for i in range(len(progresses)):
        if (100 - progresses[i]) % speeds[i] != 0:
            day =  (100 - progresses[i]) // speeds[i] + 1
        else:
            day = (100 - progresses[i]) // speeds[i]
        days.append(day)

    cnt = 0
    max_day = days[0]

    for i in range(len(days)):
        if days[i] <= max_day:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1
            max_day = days[i]

    answer.append(cnt)

    return answer