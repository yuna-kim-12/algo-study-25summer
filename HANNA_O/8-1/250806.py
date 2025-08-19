# 구간합 (List 1-1)

# 아이디어
# 1. T, N, M, 정수 리스트 받아오기
# 2. 0부터 N-M+1까지 M개의 합 구하기
# 3. 만약 그 값이 갱신된 최소값보다 작거나 최대값보다 크다면 갱신
# 4. 최대값 - 최소값 출력

T = int(input())

for TC in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    mini, maxi = sum(arr[:M]), sum(arr[:M])

    for i in range(N-M+1):
        total = sum(arr[i:i+M])
        if total < mini:
            mini = total
        elif total > maxi:
            maxi = total

    print(f'#{TC} {maxi - mini}')
