# Compute the intersection of two sorted arrays

# Solution 1, optimal if one list is much larger than the other
def intersect_two_sorted_arrays(l1, l2):
    ret = []
    for n in l1:
        if n in l2:
            ret.append(n)
    return ret

# Solution 2
def intersect_two_sorted_arrays(l1, l2):
    ret = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if (l1[i] == l2[j]) and (i == 0 or l1[i] != ret[-1]):
            ret.append(l1[i])
            i += 1
            j += 1
        elif l1[i] < l2[j]:
            i += 1
        else:
            j += 1
    return ret
