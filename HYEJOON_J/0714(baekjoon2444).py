# 별찍기 7

N = int(input())

j = N - 1
for i in range(1, 2 * N, 2):
    print((j * " ") + (i * "*"))
    j -= 1

z = 1
for i in range(2 * N - 3, 0, -2):
    print((z * " ") + (i * "*"))
    z += 1
