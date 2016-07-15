# Enumerate all primes to n.
def gen_primes(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[0], is_prime[1] = False, False
    ret = []
    for p in range(2, n + 1):
        if is_prime[p]:
            ret.append(p)
            j = p + p
            while j <= n:
                is_prime[j] = False
                j += p
    return ret

# Test.
case = 18
print gen_primes(case)
