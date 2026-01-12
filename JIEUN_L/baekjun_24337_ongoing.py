import sys
sys.stdin = open("input.txt")  #제출 시 open 부분 삭제

""""
어쩻든 큰 수가 맨 뒤로 가는게 제일 나음. 앞은 무조건 1로 시작. 
일단 b를 기준으로 생각해도 될 것 같음. 
1. 만일 b보다 a가 크다면 
맨 끝에서 1부터 시작해 b까지 순차적으로 쓰고, 그 다음부턴 a-1부터 1까지. 
2. 만일 a가 b보다 크다면 맨 끝에서부터 b-1까지 쓰고, 그 다음부턴 a부터 1까지 씀. 
3. N> a+b-1라면 0부터 남은 인덱스까지 전부 1로 채움

불가능 조건 
N <a+b-1 인 경우 
예외조건 : 
a=1인 경우 앞에 1이 오면 안됨 
건물들의 높이 정보가 1개 이상 존재하는 경우 N개의 건물 높이 정보 중 사전순으로 가장 앞선 것을 출력해 주세요. 출력 형식은 다음을 만족해야 합니다.

1번 건물, ... , N번 건물의 높이를 공백으로 구분해서 출력해 주세요. 출력하는 수들이 모두 다를 필요는 없습니다.
높이는 1보다 크거나 같은 정수여야 합니다.
문제의 조건에 맞는 건물들의 높이 정보가 존재하지 않으면 첫 줄에 -1을 출력해 주세요.

제한
1 ≤ N ≤ 105
"""

N, a, b = map(int, input().split())
building = [0]*(a+b-1)
if N < a+b-1 : 
    print(-1)

else : 
    # ones =  ['1']*(N-(a+b-1))
    for i in range(1, a) : # a-1개는 1부터 a까지 순차적으로.
        building[i-1] = i
    print(building)

    for i in range(b-1, 0, -1) : 
        building[a+b-i-1] = i
    print(building)
    if a == 1 :
        building[0] = 1
        ones = [str(b)]+['1']*(N-(a+b-2))
    else : 
        ones = ['1']*(N-(a+b-1))
        if a>= b : 
            building[a-1] = a
        else :
            building[a-1] = b 
    building = list(map(str, building))
    if a == 1 : 
        print(" ".join(building+ones))
    else : 
        print(" ".join(ones+building))

    