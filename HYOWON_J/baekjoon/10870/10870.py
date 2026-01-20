n = int(input())

arr = [0]*(n+1)
if n == 0 :
    print(0)
elif n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    arr[0] = 0
    arr[1] = 1
    arr[2] = 1
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]

    print(arr[n])