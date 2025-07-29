# 아이디어
# 1. 일단 A~Z 까지 전부 다 배열로 몇번째 키((최소))에 있는지 확인. A~Z는 전부 아스키코드로 ord인가? 그걸로 보자.
# 아니당... 그냥 그 딕셔너리로 먼저 만들어주자. 
# a 그리고 for문으로 보면서 키맵이 0이면 리턴 -1하는걸로.




def solution(keymap, targets):
    answer = [-1]*len(targets)
    keys  = {
        'A' : 101, 
        'B' : 101, 
        'C' : 101, 
        'D' : 101, 
        'E' : 101, 
        'F' : 101, 
        'G' : 101, 
        'H' : 101, 
        'I' : 101, 
        'J' : 101, 
        'K' : 101, 
        'L' : 101, 
        'M' : 101, 
        'N' : 101, 
        'O' : 101, 
        'P' : 101, 
        'Q' : 101, 
        'R' : 101, 
        'S' : 101, 
        'T' : 101, 
        'U' : 101, 
        'V' : 101, 
        'W' : 101, 
        'X' : 101, 
        'Y' : 101, 
        'Z' : 101 
    }
    
    for i in range(len(keymap)) : 
        for j in range(len(keymap[i])) :
            keys[keymap[i][j]] = min(keys[keymap[i][j]], j+1)
    print(keys)

    for i in range(len(targets)) : 
        temp = 0
        for k in targets[i] : 
            if keys[k] == 101 : 
                temp = -1
                break
            temp += keys[k]
        answer[i] = temp

    print(answer)
    return answer


solution(["AA", "ABV"], 	["B", "C", "VVVA"])