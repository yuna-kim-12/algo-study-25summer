from math import comb

# n, m = map(int, input().split())
n = 100
m = 6
## 방법1
# print(comb(n, m))

## 방법2
# up = 1
# down = 1
#
# for i in range(n - m + 1, n+1):
#     up *= i
#
# for i in range(2, m+1):
#     down *= i
#
# print(up//down)


##방법 3
# m = min(m, n-m)
# res = 1
#
# for i in range(1, m+1):
#     res *= n - i + 1
#     res //= i
#
# print(res)