import sys
sys.stdin = open("num.txt")

N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()

plus = []
zero = []
one = []
minus = []
answer = 0

#-,0,1,+ 나누기
for i in arr:
    if i > 1:
        plus.append(i)
    elif i == 1:
        one.append(i)
    elif i == 0:
        zero.append(i)
    else:
        minus.append(i)

def calculate(arr, arr_len):
    global answer
    for i in range(0, arr_len, 2):
        answer += arr[i] * arr[i + 1]
    return

if minus:
    if len(minus) % 2 == 0:
        calculate(minus, len(minus))
    else:
        if zero:
            calculate(minus, len(minus)-1)
        else:
            calculate(minus, len(minus)-1)
            answer += minus[-1]

plus.sort(reverse=True)
if plus:
    if len(plus) % 2 == 0:
        calculate(plus, len(plus))
    else:
        calculate(plus, len(plus)-1)
        answer += plus[-1]

if one:
    answer += len(one)

print(answer)