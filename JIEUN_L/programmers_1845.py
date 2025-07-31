def solution(nums):

    allowed = len(nums)//2
    nums = set(nums)
    length = len(nums)
    if length >= allowed :
        return allowed
    else : 
        return length

