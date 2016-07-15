# Compute teh spiral ordering of a 2d array.

# Solution 1
"""
def spiral_order(nums):
    ret = []
    for i in range((len(nums) + 1)/2):
        walk_one_round(nums, i, ret)
    return ret

def walk_one_round(nums, offset, ret):
    if offset == len(nums) - 1 - offset:
        ret.append(nums[offset][offset])
        return
    for j in range(offset, len(nums) - 1 - offset):
        ret.append(nums[offset][j])
    for i in range(offset, len(nums) - 1 - offset):
        ret.append(nums[i][len(nums) - 1 - offset])
    for j in range(len(nums) - 1 - offset, offset, -1):
        ret.append(nums[len(nums) - 1 - offset][j])
    for i in range(len(nums) - 1 - offset, offset, -1):
        ret.append(nums[i][offset])
"""

# Solution 2
def spiral_order(nums):
    shift = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    dir, i, j = 0, 0, 0
    ret = []
    for _ in range(len(nums) * len(nums)):
        ret.append(nums[i][j])
        nums[i][j] = 0
        new_i, new_j = i + shift[dir][0], j + shift[dir][1]
        if (new_i < 0 or new_i >= len(nums) or
            new_j < 0 or new_j >= len(nums) or 
            nums[new_i][new_j] == 0):
            dir = (dir + 1) % 4
            new_i, new_j = i + shift[dir][0], j + shift[dir][1]
        i, j = new_i, new_j
    return ret

nums = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print spiral_order(nums)
