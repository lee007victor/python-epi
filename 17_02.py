# Compute the Levenshtein distance.
def l_distance(s_a, s_b):
    dist_a2b = [[-1] * len(s_b) for _ in range(len(s_a))]
    return solver(s_a, len(s_a) - 1, s_b, len(s_b) - 1, dist_a2b)

def solver(s_a, i, s_b, j, dist_a2b):
    if s_a < 0:
        return s_b + 1
    elif s_b < 0:
        return s_a + 1
    if dist_a2b[i][j] == -1:
        if s_a[i] == s_b[j]:
            dist_a2b[i][j] = solver(s_a, i - 1, s_b, j - 1, dist_a2b)
        else:
            d_sub_last = solver(s_a, i - 1, s_b, j - 1, dist_a2b)
            d_add_last = solver(s_a, i, s_b, j - 1, dist_a2b)
            d_del_last = solver(s_a, i - 1, s_b, j, dist_a2b)
            dist_a2b[i][j] = 1 + min(d_sub_last, d_add_last, d_del_last)
        return dist_a2b[i][j]

