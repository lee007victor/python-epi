# Merge two sorted arrays.
def merge_sorted_arrays(l1, m, l2, n):
    i, j = m - 1, n - 1
    w_i = m + n - 1
    while i >= 0 and j >= 0:
        if l1[i] < l2[j]:
            l1[w_i] = l2[j]
            j -= 1
        else:
            l1[w_i] = l1[i]
            i -= 1
        w_i -= 1
    while j >= 0:
        l1[w_i] = l2[j]
        j -= 1
        w_i -= 1

# Test.
l1 = [5,13,17,None,None,None,None,None]
l2 = [3,7,11,19]
m = 3
n = 4
merge_sorted_arrays(l1, m, l2, n)
print l1
