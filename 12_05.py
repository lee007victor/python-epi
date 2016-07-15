# Compute the real square root.
def real_square_root(x):
    if x < 1.0:
        l, r = x, 1.0
    else:
        l, r = 1.0, x
    while compare(l, r):
        m = l + 0.5*(r - l)
        m2 = m * m
        res = compare(m2, x)
        if res == 0:
            return m
        elif res > 0:
            r = m
        else:
            l = m
    return l

def compare(a, b):
    err = 0.00001  # precision 
    diff = (a - b)/b
    if diff > err:
        return 1
    elif diff < -err:
        return -1
    else:
        return 0

# Test.
test_cases = [0.5, 1, 1.0, 7]
for c in test_cases:
    print real_square_root(c)
