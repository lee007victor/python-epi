# Generate the power set. 

# Solution 1: my own.
def power_set_sol1(nums):
    ret = [[]]
    sol1_helper(nums, ret)
    return ret

def sol1_helper(nums, ret):
    if not nums:
        return
    curr = nums[-1]
    sol1_helper(nums[:-1], ret)
    # Cannot use ret += ret[:] here because each element will still be a
    # reference!
    ret += [list(r) for r in ret]
    for i in range(len(ret)/2, len(ret)):
        ret[i].append(curr)

# Solution 2: epi book sol 1
def power_set_sol2(nums):
    ret = []
    sol2_helper(nums, 0, [], ret)
    return ret

def sol2_helper(nums, i, res, ret):
    print i, res
    if i == len(nums):
        ret.append(res[:])
        return
    res.append(nums[i])
    sol2_helper(nums, i + 1, res, ret)
    res.pop()
    sol2_helper(nums, i + 1, res, ret)

# Solution 3: epi book sol 2
import math

def power_set_sol3(nums):
    ret = []
    for i in range(1 << len(nums)):
        curr = []
        while i:
            curr.append(nums[int(math.log(i & ~(i - 1), 2))])
            i &= (i - 1)
        ret.append(curr)
    return ret

# Test.
test_case = [0, 1, 2]
print power_set_sol3(test_case)
