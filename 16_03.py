# Generate permutations.
def generate_permutations(l_nums):
    ret = []
    solver(l_nums[:], [], ret)
    return ret

def solver(nums, res, ret):
    if not nums:
        if res:
            ret.append(res)
        return
    for i in range(len(nums)):
        solver(nums[:i] + nums[i + 1:], res[:] + [nums[i]], ret)
