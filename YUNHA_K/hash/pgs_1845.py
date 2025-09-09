def solution(nums):
    from collections import Counter
    nums_hash = Counter(nums)
    answer = len(nums_hash)
    max_num = len(nums) / 2

    if answer > max_num:
        return max_num
    return answer