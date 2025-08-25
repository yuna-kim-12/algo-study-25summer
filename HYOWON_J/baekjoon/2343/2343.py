import sys
sys.stdin = open('txt.num')

N, M = map(int, input().split())
list_b = list(map(int, input().split()))

answer = 0
start = max(list_b)
end = sum(list_b)

while start <= end:
    mid = (start + end)//2

    cnt = 1
    sum_b = 0
    for b in list_b:
        sum_b += b
        if sum_b > mid:
            cnt += 1
            sum_b = b

    if cnt <= M:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)