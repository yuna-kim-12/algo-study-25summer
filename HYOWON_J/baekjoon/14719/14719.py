import sys
sys.stdin = open('n.txt')

#### 틀림 -> 나중에....
H, W = map(int, sys.stdin.readline().split())
b = list(map(int, sys.stdin.readline().split()))

rain = 0
stack = []

for i, h in enumerate(b):
    while stack and b[stack[-1]] < h:
        mid = stack.pop()               # 바닥(계곡의 바닥)
        if not stack:                   # 왼쪽 벽이 없으면 물 못담음
            break
        left = stack[-1]                # 왼쪽 벽
        height = min(b[left], h) - b[mid]
        width  = i - left - 1
        if height > 0:
            rain += height * width
    stack.append(i)

print(rain)