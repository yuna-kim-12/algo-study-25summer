def solution(s):
    s = s.lower()
    answer = ''
    flag = True  # 단어의 첫 글자임을 나타내는 플래그

    for char in s:
        if flag and 'a' <= char <= 'z':
            answer += char.upper()
            flag = False
        else:
            answer += char
            if char == ' ':
                flag = True
            else:
                flag = False

    return answer