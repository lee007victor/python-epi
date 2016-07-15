# Reverse digits.
def reverse_num(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    ret = 0
    while n:
        ret = ret * 10 + n % 10
        n /= 10
    return sign * ret

# Test.
cases = [-123, -1, 0 , 1, 321]
for c in cases:
    print reverse_num(c)
