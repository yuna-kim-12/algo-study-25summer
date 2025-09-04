# 전기버스 (List 1-2)

# 아이디어
# 1. T, K, N, M, M개의 정류장 번호 리스트 받아오기
# 2. 인접한 충전소 사이의 거리가 K보다 크면 도착 불가능(break)
# 3. 현재 위해에서 다음 충전소까지 한번에 갈 수 없다면 충전
# 4. 충천 횟수 출력하기

import sys
sys.stdin = open('./sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    M_lst = [0] + list(map(int, input().split())) + [N]
    cur_loc = 0
    cnt = 0

    for i in range(1, M + 2):
        if M_lst[i] - M_lst[i - 1] > K:
            cnt = 0
            break

        if M_lst[i] - cur_loc > K:
            cur_loc = M_lst[i - 1]
            cnt += 1


    print(f'#{tc} {cnt}')



