def solution(A, B):
    answer = 0
    N = len(A)
    current_A = A

    if A == B:
        return answer

    for _ in range(N):
        last_A = current_A[-1]
        remaining_A = current_A[:-1]
        current_A = last_A + remaining_A
        answer += 1

        if current_A == B:
            return answer

    return -1