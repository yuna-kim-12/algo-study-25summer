import sys
sys.stdin = open('n.txt')

n, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()

##흐름은 이해하겠는데.. 음
#목적은 가까운 공유기 사이의 최대거리 => mid로 표현
#mid 기준으로 공유기 설치할 수 있는지 확인 => for문으로 좌표 값 확인
#공유기 수가 많거나 같다면 최대거리 늘려 -> start = mid + 1
#공유기 수가 작다면 최대거리 줄여 => end = mid - 1

start = 1
end = arr[-1] - arr[0]

while start <= end:
    mid = (start + end) //2
    current = arr[0]
    count = 1

    for i in range(1, len(arr)):
        if arr[i] >= current + mid:
            count += 1
            current = arr[i]

    if count >= c:
        start = mid + 1
    else:
        end = mid - 1

print(end)