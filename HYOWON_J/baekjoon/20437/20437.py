import sys
sys.stdin = open('n.txt')

T = int(input())
answer = []

for _ in range(T):
    dict = {}
    W = list(str(input()))
    K = int(input())

    for idx , ch in enumerate(W):
        if ch not in dict:
            dict[ch] = []
        dict[ch].append(idx)

    min_idx = int(1e9)
    max_idx = 0

    for idxs in dict.values():
        if len(idxs) >= K:
            for i in range(0, len(idxs) - K + 1):
                min_idx = min(min_idx, idxs[K - 1 + i] - idxs[i] + 1)
                max_idx = max(max_idx, idxs[K - 1 + i] - idxs[i] + 1)


    if min_idx == int(1e9):
        answer.append([-1])
    else:
        answer.append([min_idx, max_idx])

for i in answer:
    print(*i)