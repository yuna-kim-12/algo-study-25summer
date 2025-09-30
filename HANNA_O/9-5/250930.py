# programmers 같은 숫자는 싫어 (스택, 큐)

# 아이디어
# 1. 숫자 하나씩 꺼내기
# 2. 현재 숫자가 방금 전 꺼낸 숫자와 다르다면 새로운 배열에 넣기
# 3. 새로운 배열 출력하기

def solution(arr):
    answer = []

    for i in range(len(arr)):
        if i == 0:
            answer.append(arr[0])
        elif answer[-1] != arr[i]:
            answer.append(arr[i])

    return answer