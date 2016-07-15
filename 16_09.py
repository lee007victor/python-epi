# Implement a Sudoku solver.
def sudoku_solver(a):
    return helper(0, 0, a)

def helper(i, j, a):
    if j == len(a[i]):
        j = 0
        i += 1
        if i == len(a):
            return True
    if a[i][j] != 0:
        return helper(i, j + 1, a)
    for n in range(1, len(a[0]) + 1):
        if is_valid(a, i, j, n):
            a[i][j] = n
            if helper(i, j + 1, a):
                return True
    a[i][j] = 0
    return False

def is_valid(a, i, j, val):
    for v in a[i]:
        if v == val:
            return False
    for k in range(len(a)):
        if a[k][j] == val:
            return False
    reg_size = int(len(a) ** 0.5)
    M, N = i/reg_size*reg_size, j/reg_size*reg_size
    for m in range(reg_size):
        for n in range(reg_size):
            if a[M + m][N + n] == val:
                return False
    return True
