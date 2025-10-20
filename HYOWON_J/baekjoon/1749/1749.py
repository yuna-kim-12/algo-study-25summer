import sys
sys.stdin = open('n.txt')

#이해 못함
n, m = map(int, input().split())
arr = []
max_sum = -int(1e9)
for _ in range(n):
    a = list(map(int, input().split()))
    arr.append(a)

s = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + arr[i-1][j-1]

for x1 in range(1, n+1):
    for y1 in range(1, m+1):
        for x2 in range(x1, n+1):
            for y2 in range(y1, m+1):
                max_sum = max(max_sum, s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1])


print(max_sum)