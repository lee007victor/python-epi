# recursive, O(n) space
def calc_fibonacci_recursive(n):
    f_dict = {}
    if n < 2:
        return n
    elif n not in f_dict:
        f_dict[n] = (calc_fibonacci_recursive(n - 2)
                    + calc_fibonacci_recursive(n - 1))
    return f_dict[n]

# iterative, O(1) space
def calc_fibonacci_iterative(n):
    if n < 2:
        return n 
    else:
        pre, cur = 0, 1
        for _ in range(2, n + 1):
            ret = cur + pre
            pre, cur = cur, ret
        return ret

for i in range(6):
    print calc_fibonacci_iterative(i)
