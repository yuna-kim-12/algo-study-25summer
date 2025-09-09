import sys
input = sys.stdin.readline

sugar = int(input())

def find_bag(sugar):
    for five_bags in range(sugar//5, -1, -1):
        residual = sugar - 5*five_bags
        if residual % 3 ==0:
            three_bags = residual // 3
            return five_bags + three_bags
    return -1

print(find_bag(sugar))