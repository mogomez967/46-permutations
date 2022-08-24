from itertools import permutations

def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    result = []
    perm = permutations(nums)

    for i in perm:
        result.append(i)
        
    return result


nums = [1, 2, 3]
print(permute(nums))