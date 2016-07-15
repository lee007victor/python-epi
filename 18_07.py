# Compute the maximum water trapped by a pair of vertical lines.
def max_trapped_water(nums):
    i, j = 0, len(nums) - 1
    max_water = 0
    while i < j:
        max_water = max(max_water, min(nums[i], nums[j]) * (nums[j] - nums[i]))
        if nums[i] > nums[j]:
            i += 1
        elif nums[i] > nums[j]:
            j += 1
        else:
            i += 1
            j += 1
    return max_water
