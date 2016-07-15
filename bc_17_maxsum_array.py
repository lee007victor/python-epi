def find_maxsum_subarray(nums):
    min_sum, cur_sum, max_sum = 0, 0, 0
    for n in nums:
        cur_sum += n
        if cur_sum < min_sum:
            min_sum = cur_sum
        if cur_sum - min_sum > max_sum:
            max_sum = cur_sum - min_sum
    return max_sum
