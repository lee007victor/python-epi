# EPI 6.1 the Dutch national flag problem
# The solutions solve this problem using O(1) space

# Testing:
def test():
    for t in test_cases:
        cur_nums = list(t[0])
        DutchFlagPartition(t[0], t[1])
        print 'Input: {}, Result: {}'.format(
            cur_nums, 
            'Pass' if t[0] == t[2] else 'Wrong'
            )
        #print t[0]

"""
# Soltuion 1: brute force, two passes, O(n^2)
def DutchFlagPartition(nums, p_index):
    pivot = nums[p_index]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] < pivot:
                nums[j], nums[i] = nums[i], nums[j]
                break

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] < pivot:
            break
        for j in range(i-1, -1, -1):
            if nums[j] > pivot:
                nums[j], nums[i] = nums[i], nums[j]
            break

test_cases = [
    [[1,1,-3,0,-1,-5,1,3,4,2], 0, [-3,0,-1,-5,1,1,1,2,3,4]],
    ]

test()	
"""

"""
# Solution 2: optimized, two passes, O(n)
def DutchFlagPartition(nums, p_index):
    pivot = nums[p_index]
    smaller, larger = 0, len(nums) - 1

    for i in range(len(nums)):
        if nums[i] < pivot:
            nums[i], nums[smaller] = nums[smaller], nums[i]
            smaller += 1

    for i in range(len(nums) - 1, -1, -1):
        if nums[i] > pivot:
            nums[i], nums[larger] = nums[larger], nums[i]
            larger -= 1

test_cases = [
    [[1,1,-3,0,-1,-5,1,3,4,2], 0, [-3,0,-1,-5,1,1,1,3,4,2]],
    ]

test()
"""

# Solution 3: one pass, O(n)
# smaller group: [0, smaller-1]
# equal group: [smaller, equal-1]
# unclassified group: [equal, larger-1]
# larger group: [larger, len(nums)-1]
def DutchFlagPartition(nums, p_index):
    pivot = nums[p_index]
    smaller, equal, larger = 0, 0, len(nums)-1

    while equal < larger:
        if nums[equal] < pivot:
            nums[equal], nums[smaller] = nums[smaller], nums[equal]
            smaller += 1
            equal += 1
        elif nums[equal] == pivot:
            equal += 1
        else:  # nums[equal] > pivot
            nums[equal], nums[larger] = nums[larger], nums[equal]
            larger -= 1

test_cases = [
    [[1,1,-3,0,-1,-5,1,3,-1,4,1,2], 0, [-3,0,-1,-5,-1,1,1,1,1,4,2,3]],
    ]

test()
