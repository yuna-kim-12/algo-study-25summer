# 삼성시의 버스 노선, 너 오랜만이다

# 입력: N 버스 노선 갯수, Ai 이상 Bi 이하 버스 정류장, P 버스 정류장 수, C번 정류장 지나는 버스 노선 갯수

# 출력: p개의 각 버스 정류장에 몇개의 버스 노선

# 아이디어:
# 2. 인풋받은 A~B까지의 버스 노선 정보를 인덱스 기반 빈 딕셔너리에 저장해둔다
# 3. P개 인풋받고, 2차원 행렬을 만든다. 2차원 [] 빈행렬을 0으로 P개마다 채운다
# 4. 노선 정보를 가지고 2차원 빈 행렬을 1로 채운다
# 5. 행렬을 순회하며 카운트(1행 1열, 2행 1열 ... 열은 같되 행이 다르게 순회 -> 그 다음 열에서 반복)
# 6. 각 세로줄마다 파악 완료 후 빈 리스트에 카운트 합을 넣고, 최종적으로 공백 두고 출력


# --------------- 테케 1개라 맞긴한데 공포의 for 문 반복 -> 런타임에러 났따 역시
from collections import defaultdict

T = int(input())
for t in range(1, T + 1):
    N = int(input())  # 버스 노선 갯수
    lines = defaultdict(list)
    for n in range(N):
        A, B = map(int, input().split())  # A~B 노선
        for num in range(A - 1, B):
            lines[n].append(num)

    P = int(input())  # 버스 정류장 수
    for _ in range(P):
        C = int(input())  # C번 정류장 지나는 노선 수

    matrix = [[0 for _ in range(P)] for _ in range(N)]  # 노선 갯수만큼

    for key, value in lines.items():
        for v in value:
            matrix[key][v] = 1

    results = []  # 각 노선마다 정류장 수

    # 각 노선마다 정류장 수 카운트
    for j in range(P):
        count = 0
        for i in range(N):
            if matrix[i][j] == 1:
                count += 1
        results.append(count)

    print(f"#{t}", *results, sep=" ")

# -------------------------------------------------------------------------
# 아 충격 작년에 푼 답
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = [0] * 5001

    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B + 1):
            cnt[i] += 1

    P = int(input())
    print(f"#{tc}", end=" ")
    for _ in range(P):
        print(cnt[int(input())], end=" ")
    print()
