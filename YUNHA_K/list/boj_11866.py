N, K = map(int, input().split())

lst = list(i for i in range(1,N+1))
answer = []
pointer = 0

while lst:
    pointer = (pointer + K - 1) % len(lst)
    answer.append(str(lst.pop(pointer)))

print('<'+', '.join(answer)+'>')