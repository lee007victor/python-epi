# Reverse all words in a sentence.
def reverse_string(l_s):
    reverse(l_s, 0, len(l_s))
    i, j = 0, find_char(l_s, 0, ' ')
    while j != -1:
        reverse(l_s, i, j)
        i, j = j + 1, find_char(l_s, j + 1, ' ')
    reverse(l_s, i, len(l_s))

def reverse(l_s, m, n):
    if m >= n:
        return
    n -= 1
    rounds = (n - m)/2 + 1
    for i in range(rounds):
        l_s[m + i], l_s[n - i] = l_s[n - i], l_s[m + i]

def find_char(l_s, start, char):
    for i in range(start, len(l_s)):
        if l_s[i] == ' ':
            return i
    return -1

# Test.
s = 'ram is costly'
l_s = list(s)
reverse_string(l_s)
print ''.join(l_s)
