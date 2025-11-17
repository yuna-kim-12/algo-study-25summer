def solution(arr, intervals):
    (a1, b1), (a2, b2) = intervals
    answer = arr[a1:b1+1] + arr[a2:b2+1]
    return answer