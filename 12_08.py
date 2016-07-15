# Find the k-th largest element
import random

def find_kth_largest(nums, k):
    l, r = 0, len(nums) - 1
    while l <= r:
        p = random.randint(l, r)
        new_p = p_partition(l, r, p, nums)
        if new_p == k - 1:
            return nums[new_p]
        elif new_p > k - 1:
            r = new_p - 1
        else:
            l = new_p + 1

def p_partition(l, r, p, nums):
    p_val = nums[p]
    new_p = l
    nums[p], nums[r] = nums[r], nums[p]
    for i in range(l, r):
        if nums[i] > p_val:
            nums[i], nums[new_p] = nums[new_p], nums[i]
            new_p += 1
    nums[r], nums[new_p] = nums[new_p], nums[r]
    return new_p

# Test.
cases = [
    [3, 2, 1, 5, 4],
    [3, 1, -1, 2],
    ]

for c in cases:
    print c
    print find_kth_largest(c, 1)
    print find_kth_largest(c, 2)
    print find_kth_largest(c, 3)
