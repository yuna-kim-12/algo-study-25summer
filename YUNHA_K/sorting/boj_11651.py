import sys
input = sys.stdin.readline

N = int(input())
coordinates = []
for _ in range(N):
    coordinates.append(list(map(int, input().split())))

coordinates.sort(key=lambda x:(x[1],x[0]))

for coordinate in coordinates:
    print(*coordinate)