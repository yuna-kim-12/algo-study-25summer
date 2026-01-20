N = int(input())
#처음에 3,5로 나눠질때 분기처리 했는데 그러지 말고 처음부터 5로 최대한 나눠보고 시작.
a = N//5
answer = -1
# a를 -1 해가면서 3으로 나눌 수 있는게 있는지 확인해야함.
for _ in range(0, a+1):
    rest = N - 5 * a
    if rest % 3 == 0:
        answer = a + rest//3
        break
    a -= 1

print(answer)