import sys
sys.stdin = open("num.txt")
# from collections import  deque
#
# N = int(input())
# arr = deque()
# for _ in range(N):
#     arr.append(int(input()))
#
# answer = 0
# while len(arr) != 1:
#     sorted(arr)
#     a = arr.popleft()
#     b = arr.popleft()
#     c = a + b
#     answer = answer + c
#     arr.appendleft(c)
#
# print(answer)

# from queue import PriorityQueue
#
# N = int(input())
# arr = PriorityQueue()
# for _ in range(N):
#     arr.put(int(input()))
#
# answer = 0
# while arr.qsize() > 1:
#     a = arr.get()
#     b = arr.get()
#     c = a + b
#     answer += c
#     arr.put(c)
#
# print(answer)

import heapq

N = int(input())
arr = [int(input()) for _ in range(N)]

if N == 1:
    print(0)
else:
    heapq.heapify(arr)
    answer = 0
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        c = a + b
        answer += c
        heapq.heappush(arr, c)
    print(answer)