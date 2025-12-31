import sys
sys.stdin =  open("input.txt")

""" 이전 제출 - 통과! 
N, M = map(int, input().split())

friend = [[] for _ in range(N)]

for i in range(M) : 
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)

def DFS(friend, me, visited, chain_cnt, answer) : 
    if chain_cnt >= 5 : 
        answer = 1
        return answer

    for m in friend[me] : 
        if not visited[m] : 
            visited[m] = True
            answer  = DFS(friend, m, visited, chain_cnt+1, answer)
            visited[m] = False
    
    return answer
        
visit = [False]*N

for i in range(N) : 
    visit[i] = True
    answer = DFS(friend, i, visit, 1, 0)
    if answer :
        break
    visit[i] = False

print(answer)
"""


##### 근데 이전 제출로 하려니, 이거 문제 개재미없어서 다른 방법으로 품. 

"""
문제 푸는 새로운 방법 : 
1. 일단 현재 내가 보낸 모든 경로에서 값을 리턴하도록 함. 말단은 1을 리턴함. 방문했는 노드니까 global 방문완료에 표기함. 내부 visited 에도 당근 표기해야 함.
2. 내가 받은 모든 값 중 맥스값 + 1을 리턴함. 

"""
import sys
sys.setrecursionlimit(10000)


N, M = map(int, input().split())

friend = [[] for _ in range(N)]

for i in range(M) : 
    a, b = map(int, input().split())
    friend[a].append(b)
    friend[b].append(a)
# print(friend)

def DFS(friend, me, chain_cnt,answer, visited, glob_visited) :
    if chain_cnt >= 5 : 
        # print("triggered : ", me, chain_cnt, answer)
        return 1, chain_cnt
    chains = []
    for m in friend[me] : 
        if not visited[m] :  
            visited[m] = True
            glob_visited[0][m] = True
            answer, temp_chain_cnt = DFS(friend, m, chain_cnt, answer, visited, glob_visited)
            # print(temp_chain_cnt)
            chains.append(temp_chain_cnt)
            
            visited[m] = False

    if chains : 
        chain_cnt = max(chains)
    # print(me, chain_cnt, answer)
    if chain_cnt >= 5 : 
        # print("triggered : ", me, chain_cnt, answer)
        return 1, chain_cnt
    

    return answer, chain_cnt +1

glob_visited = [[False]*N]
answer= 0
for i in range(N) : 
    if not glob_visited[0][i] :
        answer, _ = DFS(friend, i, 1, answer, [False]*N, glob_visited) 
        
        if answer : 
            break
# print(_)
print(answer)

"""
이 코드는 근본적으로 문제가 있음. 이미 자식 노드 전부 탐색하고, max값 확인할 때만 리턴하는 구조임. 즉, 백트래킹으로서 의미가 없다는 의미임. 따라서 이 코드 폐기

"""

