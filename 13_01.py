# Test for palindromic permutations.
def can_form_palindrome(s):
    c2cnt = {}
    for c in s:
        if c in c2cnt:
            c2cnt[c] += 1
        else:
            c2cnt[c] = 1

    odd_cnt = 0
    for v in c2cnt.values():
        if v % 2 != 0:
            odd_cnt += 1
            if odd_cnt > 1:
                return False
    return True
