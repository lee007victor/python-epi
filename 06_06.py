# EPI 6.6 Buy and sell a stock once

"""
# Solution 1: brute force, O(n^2)
def BuyAndSellStockOnce(nums):
    result = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            result = max(result, nums[j]-nums[i])
    return result
"""

# Solution 2: log the min stock price seen until now, one-pass, O(n)
def BuyAndSellStockOnce(nums):
    p_min, res = None, 0
    for i in range(1, len(nums)):
        if p_min is None or nums[i] < p_min:
            p_min = nums[i]
            continue
        res = max(res, nums[i] - p_min)
    return res

# Testing:
def Test():
    test_cases = [
        [[310,315,275,295,260,270,290,230,255,250], 30],
        ]
    for t in test_cases:
        cur_res = BuyAndSellStockOnce(t[0])
        print 'Input: {}, Output: {}, Result: {}'.format(
            t[0], cur_res, 'Pass' if cur_res == t[1] else 'Wrong')

Test()
