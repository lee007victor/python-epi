# Search a sorted array for the first occurance of k

def search_first_k(nums, k):
    l, r, ret = 0, len(nums) - 1, None
    while l <= r:
        m = l + (r-l)/2
        if nums[m] > k:
            r = m - 1
        elif nums[m] == k:
            ret = nums[m]
            r = m - 1
        else:
            r = m + 1
    return ret
