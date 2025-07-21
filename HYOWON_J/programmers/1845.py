# def solution(nums):
#     answer = 0
#     half_nums = len(nums) // 2
#     set_nums = set(nums)
#     len_set_num = len(set_nums)
#     if len_set_num > half_nums:
#         answer = half_nums
#     elif len_set_num <= half_nums:
#         answer = len_set_num
#     return answer

# def solution(nums):
#     answer = 0
#     nums_dict = {}
#     for i in nums:
#         nums_dict[i] = nums_dict.get(i, 0) + 1
#     len_dict = len(nums_dict)
#     half_nums = len(nums) // 2
#
#     if len_dict > half_nums:
#         answer = half_nums
#     elif len_dict <= half_nums:
#         answer = len_dict
#
#     return answer

def solution(nums):
    answer = min(len(nums)//2, len(set(nums)))
    return answer


print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))
