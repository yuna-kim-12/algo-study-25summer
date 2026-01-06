import sys
#문제 상에서 10만줄 이상 인풋할 수 있음
#대량 입력 최적화해야함.
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
count = 0

#인상하지 않아도 통과되는 경우
for _ in range(N):
    a,b = map(int, input().split())
    if a < b:
        arr.append(b - a)
    else:
        count += 1
if count >= K:
    print(0)

#인상해야 통과되는 경우
else :
    arr.sort()
    print(arr[K-count-1])