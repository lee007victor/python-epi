# The Sudoku checker problem.
def is_valid_sudoku(nums):
    for i in range(len(nums)):
        if not valid_range(nums, i, i + 1, 0, len(nums[0])):
            return False
    for j in range(len(nums[0])):
        if not valid_range(nums, 0, len(nums), j, j + 1):
            return False
    range_size = len(nums) ** 0.5
    for i in range(range_size):
        for j in range(range_size):
            if not valid_range(nums, i * range_size, (i + 1) * range_size, 
                               j * range_size, (j + 1) * range_size):
                return False
    return True

def valid_range(nums, row_s, row_e, col_s, rol_e):
    dups = set([])
    for i in range(row_s, row_e):
        for j in range(col_s, col_e):
            if (nums[i][j] != 0 and nums[i][j] not in dups):
                dups.add(nums[i][j])
            else:
                return False
    return True
