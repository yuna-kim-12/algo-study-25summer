import sys
sys.stdin = open('n.txt')

arr = input()
a = arr.count('a')

arr += arr

count = int(1e9)

for i in range(len(arr)-(a-1)):
    count = min(count, arr[i:i+a].count('b'))

print(count)