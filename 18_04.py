# The 3-sum problem.
def has_three_sum(nums, t):
    nums.sort()
    for n in nums:
        if has_two_sum(nums, t - n):
            return True
    return False

def has_two_sum(nums, t):
    i, j = 0, len(nums) - 1
    while i < j:
        cur_sum = nums[i] + nums[j]
        if cur_sum < t:
            i += 1
        elif cur_sum == t:
            return True
        else:
            j -= 1
    return False
