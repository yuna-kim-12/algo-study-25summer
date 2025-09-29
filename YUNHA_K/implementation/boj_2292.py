N = int(input())

final_num = 1
i = 2

if N == 1:
    print(1)
else:
    while True:
        final_num += 6*i - 6
        if N <= final_num:
            break
        i += 1
    print(i)
