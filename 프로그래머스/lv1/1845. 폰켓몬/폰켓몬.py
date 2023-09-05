def solution(nums):
    n = len(nums) / 2
    speices = len(set(nums))
    if n > speices:
        return speices
    return n