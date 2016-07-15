# Increase an arbitray-precison integer
def plus_one(nums):
    nums[-1] += 1
    i = len(nums) - 1
    while i > 0 and nums[i] == 10:
        nums[i] = 0
        i -= 1
        nums[i] += 1
    if nums[0] == 10:
        nums[0] = 0
        nums.insert(0, 1)
    return nums

# Test.
cases = [
    [1,2,9],
    [9,9,9],
    ]

for c in cases:
    plus_one(c)
    print c
