import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key=lambda x:(x[1],x[0]))

answer = 0
last_end_time = 0
for start, end in meetings:
    if start >= last_end_time:
        answer += 1
        last_end_time = end

print(answer)