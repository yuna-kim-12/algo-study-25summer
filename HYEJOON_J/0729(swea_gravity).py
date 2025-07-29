# 입력: 가로 N 세로 100 2차원 행렬(박스)
# 출력: 가장 큰 낙차

# 맨 첫번째 값과 그 다음에 오는 수와의 차이 비교
# - 더 큰가?(더 커야 낙차가 존재) 세기: 빌딩 끝번호까지 순회
# - 작으면 카운트하지말고 다음 번호 순회

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    gravity = list(map(int, input().split()))

    max_fall = 0
    for i in range(N):
        cnt = 0
        for j in range(i + 1, N):
            if gravity[i] > gravity[j]:
                cnt += 1

            if cnt > max_fall:
                max_fall = cnt

    print(f"#{test_case} {max_fall}")
