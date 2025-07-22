def solution(arr):
    row_len = len(arr)
    col_len = len(arr[0])

    if row_len > col_len:
        cnt = row_len - col_len
        for i in arr:
            for _ in range(cnt):
                i.append(0)
        return arr

    elif col_len > row_len :
        cnt = col_len - row_len
        for i in range(cnt) :
            arr.append([0 for _ in range(col_len)])
        return arr

    else :
        return arr


print(solution([[572, 22, 37], [287, 726, 384], [85, 137, 292],[487, 13, 876]]))
print(solution([[57, 192, 534, 2], [9, 345, 192, 999]]))
print(solution([[1, 2], [3, 4]]))