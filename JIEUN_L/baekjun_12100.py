import sys
sys.stdin = open("input.txt")

"""
이정도는재귀로 풀어도 될 것 같다. 

1. 새로 맵을 만들어줘야 함.
2. dir에는 방향을 넣어줘야 함. 내가 숫자를 훝어볼 방향. 
3. for 문으로 가로든 세로든 확인.(현재 - 끝까지, 조건에 다음 블럭이 0이면 break)
4. 합쳐지는거 있으면 합치고, 아니면 그대로 업데이트.오... 근데 이거 str으로 해도 될 것 같은데? 
5. dir별로 따로 핻ㅇ동하도록 if를 만들자. 
합쳐질 때 마다 



"""

from collections import deque

#1 : 왼쪽으로 2: 오른쪽으로 3 : 위쪽으로 4 : 아래쪽으로
def shift(cnt, blocks, dir, max_val) :
    if cnt == 6 : 
        return max(map(max, blocks))

    new_block = []
    if dir == 0 : 
        for i in range(1, 5) : 
            max_val = max(max_val, shift(cnt, blocks, i, 0))
        return max_val
    elif dir ==1 : 
        for i in range(N) : 
            
            q = deque([blocks[i][0]])
            for j in range(1, N) : 
                # q에 들어왔는데 동일함
                if blocks[i][j] == 0 : 
                    pass
                elif q[-1] == blocks[i][j] : 
                    q.pop()
                    q.append(2*blocks[i][j])
                    continue
                else : 
                    q.append(blocks[i][j])
            if len(q) < N : 
                q.extend([0]*(N-len(q)))
            new_block.append(list(q))
            
    elif dir == 2 : 
        for i in range(N) : 
            q = deque([blocks[i][0]])
            for j in range(1, N) : 
                # q에 들어왔는데 동일함
                if q[0] == blocks[i][j] : 
                    q.popleft()
                    q.appendleft(2*blocks[i][j])
                else : 
                    q.appendleft(blocks[i][j])
            if len(q) < N : 
                q.extendleft([0]*(N-len(q)))
            new_block.append(list(q))
                
    elif dir == 3 : 
        for i in range(N) : 
            q = deque([blocks[0][i]])
            for j in range(1, N) : 
                # q에 들어왔는데 동일함
                if q[-1] == blocks[j][i] : 
                    q.pop()
                    q.append(2*blocks[j][i])
                else : 
                    q.append(blocks[j][i])
            if len(q) < N : 
                q.extend([0]*(N-len(q)))
            new_block.append(list(q))
        # new block transpose 
        new_block = [list(row) for row in zip(*new_block)]
    elif dir == 4 : 
        for i in range(N) : 
            q = deque([blocks[N-1][i]])
            for j in range(N-2, -1, -1) : 
                # q에 들어왔는데 동일함
                if q[0] == blocks[j][i] : 
                    q.popleft()
                    q.appendleft(2*blocks[j][i])
                else : 
                    q.appendleft(blocks[j][i])
            if len(q) < N : 
                q.extendleft([0]*(N-len(q)))
            
            new_block = [list(q)]+new_block
        # new block transpose 
        new_block = [list(row) for row in zip(*new_block)]
    if dir == 1 and cnt == 1 : 
        print(new_block)
    
    for i in range(1, 5) : 
        max_val = max(max_val, shift(cnt+1, new_block, i, max_val))
    
    return max_val
    



N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]
if N == 1 : 
    print(blocks[0][0])
else :    
    print(shift(1, blocks, 0, 0))