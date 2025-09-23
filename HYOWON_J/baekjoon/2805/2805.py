import sys
sys.stdin = open('n.txt')

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)
answer = 0

while start <= end:
    total = 0
    mid = (start + end) //2

    for i in tree:
        if i > mid :
            total += (i-mid)

    if m > total:
        end = mid - 1
        answer = end
    else:
        start = mid + 1


print(answer)