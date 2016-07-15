# Count the number of ways to traverse a 2-D array.
def num_of_ways(m, n):
    res = [[0] * n for _ in range(m)]
    return solver(m - 1, n - 1, res)

def solver(i, j, res):
    if (i == 0 and j == 0):
        return 1
    if res[i][j] == 0:
        ways_top = 0 if i == 0 else solver(i - 1, j, res)
        ways_left = 0 if j == 0 else solver(i, j - 1, res)
        res[i][j] = ways_top + ways_left
    return res[i][j]

# Test.
print num_of_ways(5, 5)
