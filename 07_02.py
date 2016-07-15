# Base conversion.
c2d, d2c = {}, {}
for i in range(16):
    h = hex(i)[-1]
    c2d[h] = i
    d2c[i] = h

def convert_base(string, b1, b2):
    is_neg = True if string[0] == '-' else False
    start = 1 if is_neg else 0
    x = 0
    for s in string[start:]:
        x *= b1
        x += c2d[s]

    sign = '-' if is_neg else ''
    return '0' if x == 0 else sign + construct_base(x, b2)

def construct_base(n, b):
    return '' if n == 0 else construct_base(n / b, b) + d2c[n % b]

# Test.
cases = [
    ('0', 10, 16),
    ('-1', 10, 16),
    ('615', 7, 13),
    ]

for c in cases:
    print convert_base(c[0], c[1], c[2])
