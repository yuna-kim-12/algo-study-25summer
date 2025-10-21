import sys
sys.stdin = open('n.txt')

s = input()
bomb = input()

stack = []
L = len(bomb)
last = bomb[-1]
b_list = list(bomb)

for ch in s:
    stack.append(ch)
    if ch == last and len(stack) >= L:
        # print(stack[-L:], L)
        if stack[-L:] == b_list:
            del stack[-L:]

if stack:
    print("".join(stack))
else:
    print('FRULA')