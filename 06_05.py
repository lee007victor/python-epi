# Delete duplicates from a sorted array.
def del_dups(nums):
    if not nums:
        return 0
    wr_id = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[wr_id - 1]:
            nums[wr_id] = nums[i]
            wr_id += 1
    for j in range(wr_id, len(nums)):
        nums[j] = 0
    return wr_id

# Test.
case = [2, 3, 5, 5, 7, 11, 11, 11, 13]
print del_dups(case)
print case
