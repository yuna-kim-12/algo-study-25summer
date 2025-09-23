# 글자 이어 붙여 문자열 만들기

def solution(my_string, index_list):
    answer = ''
    for i in range(len(index_list)):
        answer += my_string[index_list[i]]
    return answer