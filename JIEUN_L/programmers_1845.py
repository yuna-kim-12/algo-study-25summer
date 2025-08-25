def solution(nums):

    allowed = len(nums)//2
    nums = set(nums)
    length = len(nums)
    if length >= allowed :
        a = divmod(2, 4)
        return allowed
    else : 
        return length

