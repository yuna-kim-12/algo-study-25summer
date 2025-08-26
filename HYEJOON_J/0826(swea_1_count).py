T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = input()
    cnt = 0
    max_cnt = 0


    for i in range(N):
        if int(arr[i]) == 0:
            if cnt:
                if max_cnt < cnt:
                    max_cnt = cnt
            cnt = 0
        else:
            cnt += 1
            #수열이 1로 끝난다면 마지막까지 cnt한게 최대값인지
            if i == N-1:
                if max_cnt < cnt:
                    max_cnt = cnt


    print(f'#{tc}', max_cnt)