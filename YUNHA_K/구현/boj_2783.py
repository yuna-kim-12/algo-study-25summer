X, Y = map(int, input().split())
xy_price = X * (1000/Y)
N = int(input())
min_price = xy_price
for _ in range(N):
    A, B = map(int, input().split())
    ab_price = A * (1000/B)
    if min_price > ab_price:
        min_price = ab_price

print(round(min_price,2))