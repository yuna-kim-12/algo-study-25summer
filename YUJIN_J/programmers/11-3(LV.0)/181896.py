def solution(num_list):
    answer = -1  # 기본값: 음수가 없을 때 -1 반환
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            break
    return answer