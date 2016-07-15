# The Euclidean algorithm for calculating the greatest common divisor of two
# numbers

def cal_gcd(x, y):
    return x if y == 0 else cal_gcd(y, x % y)

print cal_gcd(156, 36)
print cal_gcd(36, 156)
