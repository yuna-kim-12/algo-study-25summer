import sys
input = sys.stdin.readline
def get_average(nums,N):
    avg = int(round(sum(nums)/N,0))
    return avg
def get_median(nums,N):
    median = sorted(nums)[N//2]
    return median
def get_frequent_num(nums):
    from collections import Counter
    num_count = Counter(nums)
    max_count = num_count.most_common(1)[0][1]
    max_items = [item for item, count in num_count.items() if count == max_count]
    if len(max_items) == 1:
        return  max_items[0]
    else:
        return sorted(max_items)[1]
def get_range(nums):
    return max(nums) - min(nums)


N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

print(get_average(nums,N))
print(get_median(nums,N))
print(get_frequent_num(nums))
print(get_range(nums))