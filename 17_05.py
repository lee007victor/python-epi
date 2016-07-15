# Search for a sequence in a 2-D array
def seq_in_2d_array(a, s):
    f_set = set([])
    for i in range(len(a)):
        for j in range(len(a[i])):
            if solver(a, i, j, s, 0, f_set):
                return True
    return False

def solver(a, i, j, s, m, f_set):
    if m == len(s):
        return True
    if (i < 0 or i >= len(a) or j < 0 or j >= len(a[i]) or 
            (i, j, m) in f_set):
        return False
    if (solver(a, i + 1, j, s, m + 1, f_set)
            or solver(a, i - 1, j, s, m + 1, f_set)
            or solver(a, i, j + 1, s, m + 1, f_set)
            or solver(a, i, j - 1, s, m + 1, f_set)):
        return True
    else:
        f_set.add((i, j, m))
        return False
