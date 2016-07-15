# Find the duplicated and missing elements.
def find_duplicate_missing(nums):
    d_xor_m = 0
    for i in range(len(nums)):
        d_xor_m ^= i ^ nums[i]
    diff = d_xor_m & (~(d_xor_m - 1))
    d_or_m = 0
    for i in range(len(nums)):
        if i & diff != 0:
            d_or_m ^= i
        if nums[i] & diff != 0:
            d_or_m ^= nums[i]
    for n in nums:
        if n == d_or_m:
            return [d_or_m, d_or_m ^ d_xor_m]
    return [d_or_m ^ d_xor_m, d_or_m]

# Test.
test_cases = [
        (5, 3, 0, 3, 1, 2),
        ]
for c in test_cases:
    print find_duplicate_missing(c)
