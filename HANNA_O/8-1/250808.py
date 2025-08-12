# Gravity (List 1-1)

# 아이디어
# 1. T, 방 가로길이, 상자 수 리스트 받아오기
# 2. 상자 수 리스트 순회
# 2-1. 현재 상자의 수보다 작은 상자 개수 세기(현재 상자보다 오른쪽에 있는 것들만)
# 2-2. 만약 현재 낙차가 최대값 보다 크다면 낙차 갱신
# 3. 최대 낙차 출력

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    boxs = list(map(int, input().split()))
    maxi = 0

    for i in range(N):
        cur_maxi = 0
        for j in range(i+1, N):
            if boxs[i] > boxs[j]:
                cur_maxi += 1
        if cur_maxi > maxi:
            maxi = cur_maxi

    print(f'#{tc} {maxi}')
