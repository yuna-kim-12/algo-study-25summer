# View (List 1-1)

# 아이디어
# 0. 10개의 테스트 케이스, N개의 건물 개수, N개의 건물 높이 리스트
# 1. 해당 건물의 양 옆 2칸에 있는 건물 확인
# 1-1. 해당 건물이 양옆 4개의 건물보다 크다면 양옆 4개의 건물 중 가장 큰 건물과의 차이 구하기(차이 = 확보된 조망권)
# 2. 조망권 총합 출력하기

T = 10
for tc in range(1, T+1):
    N = int(input())
    buildings = list(map(int, input().split()))
    total = 0

    for i in range(2, N-2):
        maxi = max(buildings[i-2],buildings[i-1], buildings[i+1], buildings[i+2])

        if buildings[i] > maxi:
            total += buildings[i] - maxi

    print(f'#{tc} {total}')