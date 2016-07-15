# Find the smallest subarray covering all values.
# Solution 1: subarray in memory
def smallest_subarray(a, keys):
    d = {}
    for k in keys:
        d[k] = 1 if k not in d else d[k] + 1
    ret = [-1, -1]  # [start, end]
    nums_left = len(keys)
    l, r = 0, 0
    while r < len(a):
        if a[r] in d:
            d[a[r]] -= 1
            if d[a[r]] == 0:
                nums_left -= 1
        while nums_left == 0:
            if (ret == [-1, -1] || r - l < ret[1] - ret[0]):
                ret = [l, r]
            if a[l] in d:
                d[a[l]] += 1
                if d[a[l]] > 0:
                    nums_left += 1
            l += 1
        r += 1
    return ret

# Solution 2: subarray not in memory, suitable for streaming input
import collections

def smallest_subarray(a, keys):
    d = collections.OrderedDict([])
    for k in keys:
        d[k] = -1
    nums_left = len(keys)
    ret = [-1, -1]  # [start, end]
    idx = 0
    curr = next(a, None)
    while curr:
        if curr in d:
            if d[curr] == -1:
                nums_left -= 1
            del d[curr]
            d[curr] = idx
        if nums_left == 0:
            if (ret == [-1, -1] || idx - d.values()[0] < ret[1] - ret[0]):
                ret = [d.values()[0], idx]
        curr = next(a, None)
        idx += 1
    return ret
