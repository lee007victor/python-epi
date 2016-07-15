# Compute the largest rectangle under the skyline.
def find_max_rectangle(nums):
    ids, ret = [], 0
    for i in range(len(nums) + 1):
        if (not ids or (i < len(nums) and nums[ids[-1]] < nums[i])):
            ids.append(i)
        elif (i < len(nums) and nums[ids[-1]] == nums[i]):
            ids[-1] = i
        else:
            while (ids and (i == len(nums) or nums[ids[-1]] >= nums[i])):
                H = nums[ids.pop()]
                j = 0 if not ids else ids[-1]
                W = i - (j + 1)
                ret = max(ret, H * W)
            ids.append(i)
    return ret

# Test.
test_cases = (
    [1, 4, 2, 5, 6, 3, 2, 6, 6, 5, 2, 1, 3],
    )

for case in test_cases:
    print find_max_rectangle(case)
