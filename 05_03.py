# Reverse bits
def reverse_bits(num):
    word_size = 16
    bit_mask = 0xFFFF
    return (rev[num & bit_mask] << (3 * bit_mask) 
            | rev[(num >> word_size) & bit_mask] << (2 * bit_mask) 
            | rev[(num >> 2 * word_size) & bit_mask] << bit_mask 
            | rev[(num >> 3 * word_size) & bit_mask])
