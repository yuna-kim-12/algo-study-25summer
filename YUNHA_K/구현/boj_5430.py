from collections import deque
import sys
input = sys.stdin.readline

def D(queue:deque, is_reversed:bool):
    if len(queue):
        if is_reversed:
            queue.pop()
        else:
            queue.popleft()
    else:
        return "error"
    return queue

def solve(queue, is_reversed:bool):
    for x in command:
        if x == 'R':
            is_reversed = not is_reversed
        elif x == 'D':
            queue = D(queue, is_reversed)
            if queue == 'error':
                return queue
    if not is_reversed:
        return list(queue)
    else:
        return list(queue)[::-1]

# 입력
T = int(input())
for _ in range(T):
    command = input().strip()
    n = int(input())
    arr_str = input().strip()
    if n > 0:
        lst = list(map(int, arr_str[1:-1].split(",")))
    else:
        lst = []

    queue = deque(lst)
    result = solve(queue, False)

    # 출력 형식 맞추기
    if result == "error":
        print("error")
    else:
        print("[" + ",".join(map(str, result)) + "]")

