import sys
sys.stdin = open('n.txt')

T = int(input())
arr = []
for _ in range(T):
    arr.append(int(input()))

m = [0 for _ in range(11)]

m[1] = 1
m[2] = 2
m[3] = 4

for i in range(4, 11):
    m[i] = m[i-1] + m[i-2] + m[i-3]

for i in arr:
    print(m[i])