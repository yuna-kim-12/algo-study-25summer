def solution(my_string):
    answer = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        answer.append(len(my_string.split(i))-1)
    return answer