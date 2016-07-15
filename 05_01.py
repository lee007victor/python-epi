# EPI 5.1 Computing the parity of a word
# To simpify this question, assume the input is always 8-bit

"""
# Solution 1: brute force, O(n)
def Parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
"""

"""
# Solution 2: optimized brute force, only considering set bits, O(k) - k set bits
def Parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # Drop the lowest set bit
    return result
"""

# Solution 3: lookup table, O(n/L), L- word size used by the lookup table
parity_table = [0, 1, 1, 0]  # 00 - 0, 01 - 1, 10 - 1, 11 - 0
def Parity(x):
    word_size = 2
    bit_mask = int('11', 2)  # 0x11
    return (parity_table[(x >> 3*word_size) & bit_mask]
            ^ parity_table[(x >> 2*word_size) & bit_mask]
            ^ parity_table[(x >> 1*word_size) & bit_mask]
            ^ parity_table[x & bit_mask])

"""
# Solution 4: folding, O(log(n))
def Parity(x): 
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1
"""

# Test
test_case = [
    ('00000000', '0'),
    ('00000001', '1'),
    ('10000001', '0'),
    ('10001001', '1'),
    ('11111111', '0'),
    ]

def Test():
    print 'Input - Output - Answer:'
    for i, o in test_case:
        print i + ' - ' + str(Parity(int(i, 2))) + ' - ' + o

Test()
