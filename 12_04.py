# Compute the integer square root.
def square_root(k):
    l, r = 0, k
    while l <= r:
        m = l + (r - l)/2
        m_sq = m ** 2
        if m_sq > k:
            r = m - 1
        elif m_sq == k:
            return m
        else:
            l = m + 1
    return r

# Test.
cases = [300, 21, 25]
for c in cases:
    print square_root(c)
