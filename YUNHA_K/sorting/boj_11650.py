N = int(input())
spots = []
for _ in range(N):
    x, y = map(int, input().split())
    spots.append((x,y))

spots.sort(key=lambda x:(x[0],x[1]))

for x, y in spots:
    print(x, y)