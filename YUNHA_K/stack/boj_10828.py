import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    val = list(input().split())
    if len(val) == 2:
        command, num = val
        if command == 'push':
            stack.append(int(num))
    else:
        command = val[0]
        if command == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command == 'size':
            print(len(stack))
        elif command == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif command == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)