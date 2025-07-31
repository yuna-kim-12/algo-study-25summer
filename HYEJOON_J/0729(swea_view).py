# 입력: 건물 갯수, 높이
# 출력:조망권(왼, 우 거리 2이상 비어있을 때) 확보 세대 수
# 조건: 맨왼쪽 둘, 맨 오른쪽 둘은 비어있어야한다


for i in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))
    houses = 0

    # 양옆 두칸은 빈집이어야한다 조건 충족
    for j in range(2, N - 2):
        curr_h = heights[j]
        # 내 이웃 2거리 빈집인가 확인
        max_h = max(heights[j - 2], heights[j - 1], heights[j + 1], heights[j + 2])
        # 빈집 세대만큼 차이를 센다
        if curr_h > max_h:
            houses += curr_h - max_h

    print(f"#{i} {houses}")
