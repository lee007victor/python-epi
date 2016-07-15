# Generate all nonattacking ps of n-queens
def n_queens(n):
    ret = []
    solver(n, 0, [], ret)
    return ret

def solver(n, r, p, ret):
    if r == n:
        ret.append(p)
    else:
        for c in range(n):
            p.append(c)
            if is_valid(p):
                solver(n, r + 1, p, ret)
            p.pop()

def is_valid(p):
    r = len(p) - 1
    for i in range(r):
        diff = abs(p[r] - p[i])
        if (diff == 0 or diff == r - i):
            return False
    return True
