# Check if a decimal integer is a palindrome.
import math

def is_palindrome_number(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    num_zero = int(math.log10(n))
    mask = 10 ** num_zero
    while n:
        if n / mask != n % 10:
            return False
        n %= mask
        n /= 10
        mask /= 100
    return True

# Test.
test_cases = [-1, 12, 100, 0, 1, 7, 11, 121, 333, 2147447412]
for case in test_cases:
    print is_palindrome_number(case)
