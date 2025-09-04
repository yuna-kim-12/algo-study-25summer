import sys
sys.stdin = open('num.txt')

n, m = map(int, input().split())
check = [i for i in range(n+1)]

def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        check[a] = b
    else:
        check[b] = a

    return

def find(x):
    if check[x] != x:
        check[x] = find(check[x])
    return check[x]

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
