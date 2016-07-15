# Compute all mnemonics for a phone number.
def phone_mnemonic(num_str):
    ret = []
    helper(num_str, 0, '', ret)
    return ret

n2c = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def helper(num_str, i, res, ret):
    if i == len(num_str):
        ret.append(res)
    else:
        for c in n2c[int(num_str[i])]:
            helper(num_str, i + 1, res + c, ret)

# Test.
test_cases = ['2276696']
for case in test_cases:
    print phone_mnemonic(case)
