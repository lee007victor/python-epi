# Sample offline data.
import random

def random_sampling(nums, k):
    if k >= len(nums) - 1:
        return nums
    else:
        for i in range(k):
            j = random.random(i, k)
            nums[i], nums[j] = nums[j], nums[i]
