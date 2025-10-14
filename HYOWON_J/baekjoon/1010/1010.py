import sys
sys.stdin = open('n.txt')

from math import comb

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    print(comb(m, n))