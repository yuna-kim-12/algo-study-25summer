import sys
input = sys.stdin.readline

N = int(input())
stack = []
result = []
cur = 1

for _ in range(N):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        result.append("+")
        cur += 1

    if stack and stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit()

for x in result:
    print(x)