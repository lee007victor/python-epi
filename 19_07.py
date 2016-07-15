# Transform one string to another.

import collections

def transform_string(s, t, D):
    q = collections.deque([(s, 0)])
    D.remove(s)
    while q:
        cur_s, cur_d = q.popleft()
        if cur_s == t:
            return cur_d
        for i in range(len(cur_s)):
            s_start = cur_s[:i]
            s_end = cur_s[i + 1:]
            for j in range(26):
                new_s = s_start + chr(ord('a') + j) + s_end
                if new_s in D:
                    q.append((new_s, cur+d + 1))
                    D.remove(new_s)
    return -1
