# Reorder an array of integers so that even entries appear first.
def even_odd(nums):
    i, j = 0, len(nums) - 1
    while i < j:
        if (nums[i] % 2) == 0:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]
            j -= 1
