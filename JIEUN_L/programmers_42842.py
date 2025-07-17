# 가로 + 세로  = (갈색 격자 - 4)/2
# 가로 * 세로 = 노랑 격자

# 가로((갈색 격자 -4)/2 - 가로) = 노랑 격자 
# 가로^2 - 가로*((갈색 격자 -4)/2) + 노란격자 = 0
# 가로 = ((갈색격자 -4 )/2 -(+)*root(((갈색격자 -4 )/2)^2 - 4*노란격자))/2
# 그리고 노란격자 / 가로인게 세로. 
import math

def solution(brown, yellow):

    b = int((brown -4)/2 )# c=yellow 
    backside = int(math.sqrt(b*b -4*yellow))
    answer = [int((b+backside)/2)+2,int((b-backside)/2)+2]

    return answer

print(solution(24, 24))