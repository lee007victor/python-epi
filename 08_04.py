# Test for overlapping lists.
def test_overlapping(l1, l2):
    len_l1, len_l2 = length(l1), length(l2)
    if l1 > l2:
        l1 = advance(l1, len_l1 - len_l2)
    else:
        l2 = advance(l2, len_l2 - len_l1)
    while l1 and l2 and l1 != l2:
        l1, l2 = l1.next, l2.next
    return l1

def length(l):
    len_l = 0
    while l:
        len_l += 1
        l = l.next
    return len_l

def advance(l, steps):
    while steps:
        l = l.next
        steps -= 1
    return l
