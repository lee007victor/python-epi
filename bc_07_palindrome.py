# Boot camp 7 check whether a string a palindromic

def IsPalindromic(s):
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

# Unit test
test_cases = [
    ('abcba', True),
    ('abcdefggfedcba', True),
    ('abcdefghfedcba', False),
    ]

def test():
    for t in test_cases:
        print 'Input: {}, Result: {}'.format(
            t[0], 'Correct' if IsPalindromic(t[0]) == t[1] else 'Wrong')

test()
