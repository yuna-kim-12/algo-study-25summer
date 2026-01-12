import sys 
input = sys.stdin.readline
# sys.stdin = open("input.txt")

N, M = map(int, input().split())

words = dict({})
for i in range(N) :
    w = input().strip()
    words[w] = 1
for i in range(M) : 
    keys = list(input().strip().split(","))
    for i in range(len(keys)) :
        if words.pop(keys[i], None) : 
            N -=1
    print(N)
# print(N)
