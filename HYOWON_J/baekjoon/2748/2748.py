n = int(input())

a, b = 0,1

for _ in range(n):
    a, b = b, a+b

print(a)
#어처피 최종 n번째 피보나치 수만 필요함. 계속 업데이트해서 보여주는 방식. 쥑이네