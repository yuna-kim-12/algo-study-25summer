# 입력: N = 정수 갯수, M = 고려할 이웃(이어진) 갯수
# 문제:
# N개의 정수로 이루어진 lst에서 M개를 파악
# 단, M개를 다 더해서 최저, 최대값일 것
# 출력:그 차이를 구하는 것이 답(정수)
#
# 아이디어: 슬라이스
# 1. 첫번째 자리부터 순회한다
# 2. 첫번쨰 자리에서 +(M-1)개자리까지 더한다
# - 더하기 전, +(M-1)자리의 수가 len(N)-1의 인덱스를 벗어나는가 확인
# - 벗어나지 않으면(작거나 같으면) 다 더하기
# - 벗어나면 더해볼 필요없이 순회 STOP하기
# 3. 더하고나서는 최근 최대, 최소값과 비교


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    values = list(map(int, input().split()))

    i = 0
    len_values = len(values)
    max_sum = sum(values[:M])
    min_sum = sum(values[:M])

    while i + M - 1 <= len_values - 1:
        curr_values = sum(values[i : i + M])

        if curr_values >= max_sum:
            max_sum = curr_values

        elif curr_values <= min_sum:
            min_sum = curr_values

        i += 1

    print(f"#{t+1}", max_sum - min_sum)
