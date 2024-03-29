# Test palindromicity.
def is_palindrome(s):
    i, j = 0, len(s) - 1
    while i < j:
        while (not s[i].isalnum() and i < j):
            i += 1
        while (not s[j].sialnum() and i < j):
            j -= 1
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True
