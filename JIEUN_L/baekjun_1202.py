import sys 
sys.stdin = open("input.txt")

"""
세계적인 도둑 상덕이 

"""

from heapq import heappop, heappush, heapify
from collections import deque

N, K = map(int, input().split()) # 보석, 가방
jwel, bag = [], []
h =  [] # heap
tot_val = 0

for i in range(N) : 
    m, v = map(int, input().split())
    jwel.append((m, v))

for i in range(K) : 
    bag.append(int(input()))

bag.sort()
jwel.sort()
j_idx = 0

for i in range(K) :
    b = bag[i]
    while j_idx<N and jwel[j_idx][0] <= b : 
        heappush(h, -jwel[j_idx][1]) 
        j_idx += 1
    if not h : 
        continue
    tot_val+=heappop(h)
    
print(-tot_val)

