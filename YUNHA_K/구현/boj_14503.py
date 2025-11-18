import sys
input = sys.stdin.readline
# 입력
N, M = map(int, input().split())
r, c, d = map(int, input().split())
# d : 0 ~ 3 북 동 남 서
room = []
for _ in range(N):
    room.append(list(map(int, input().split())))
# 방에서 0이면 청소 안된 칸, 1이면 벽.

# 출력 : 로봇 청소기가 작동을 시작한 후 작동을 멈출 때까지 청소하는 칸의 개수를 출력한다.
# 0 후진하는 dir, 1 회전하는 dir
rear_dirs = {0:[(1,0),(0,-1)], 1:[(0,-1),(-1,0)], 2:[(-1,0),(0,1)], 3:[(0,1),(1,0)]}
dirs = ((-1,0),(0,1),(1,0),(0,-1))

is_changed = False
ans = 0

# 종료조건 : 뒤가 벽이라서 후진 불가하면 멈춤
while True:
    # 현재 r,c가 0인지 확인
    if room[r][c] == 0:
        # 1. 0이면, 현재 칸 2로 변경
        room[r][c] = 2
        ans += 1
    # 2. 주변 4칸 탐색 & 청소 안된 빈 칸 있으면
    for dir in dirs:
        nr, nc = r + dir[0], c + dir[1]
        if 0<= nr <N and 0<=nc<M and room[nr][nc] == 0:
            # 1-1. 반시계 방향으로 90도 회전 : 4번 반복
            # 바라보는 방향 기준으로 앞이 청소되지 않으면 한 칸 전진
            for _ in range(4):
                nr, nc = r + rear_dirs[d][1][0], c + rear_dirs[d][1][1]
                d = (d+3) % 4
                if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
                    r, c = nr, nc
                    is_changed = True
                    break
        # 최상단 for 문 break
        if is_changed:
            break

    if is_changed:
        is_changed = False
        continue
    # 2. 주변 4칸 탐색 & 청소 안된 빈 칸 없으면

    # 2-1. 후진 가능하면 한 칸 후진
    nr, nc = r + rear_dirs[d][0][0], c + rear_dirs[d][0][1]
    if 0<=nr<N and 0<=nc<M and room[nr][nc] != 1:
        r, c = nr, nc
        continue
    # 2-2. 벽이라서 후진할 수 없으면 작동 멈춤.
    else:
        break

print(ans)