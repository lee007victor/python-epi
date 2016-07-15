# Multiply two arbitrary-precision integers.
def multiply(nums1, nums2):
    sign = -1 if (nums1[0] < 0) ^ (nums2[0] < 0) else 1
    nums1[0], nums2[0] = abs(nums1[0]), abs(nums2[0])
    ret = [0] * (len(nums1) + len(nums2))
    for i in range(len(nums1) - 1, -1, -1):
        for j in range(len(nums2) - 1, -1, -1):
            ret[i + j + 1] += nums1[i] * nums2[j]
            ret[i + j] += ret[i + j + 1] / 10
            ret[i + j + 1] %= 10
    k = 0
    while k < len(ret) and ret[k] == 0:
        k += 1
    if k == len(ret):
        return [0]
    else:
        ret[k] *= sign
        return ret[k:]

# Test.
test_cases = [
        [[1, 9, 3, 7, 0, 7, 7, 2, 1], [-7, 6, 1, 8, 3, 8, 2, 5, 7, 2, 8, 7]],
        ]

for case in test_cases:
    print multiply(case[0], case[1])
