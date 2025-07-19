import sys
sys.stdin = open("num.txt")

N = int(input())
k = int(input())
answer = 0

start = 1
end = k #index

while start <= end:
    mid = (start+end)//2
    cnt = 0
    # mid 이하의 수가 각 행에 몇 개 있는지 누적
    for i in range(1, N+1):
        cnt += min(int(mid/i), N)
    # mid 이하의 수가 부족하면 더 큰 값에서 탐색
    if cnt < k:
        start = mid + 1
    # mid 이하의 수가 충분하면 답 후보로 저장하고 더 작은 값에서 탐색
    else:
        answer = mid
        end = mid - 1

print(answer)
## 이진 탐색 넘 어렵ㄴ다.......