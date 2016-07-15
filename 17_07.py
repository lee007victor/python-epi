# The bedbathandbeyond.com problem.
def decompose_into_words(s, d):  # s is string, d is dictionary
    cache = [-1 for _ in range(len(s))]
    for i in range(len(s)):
        if s[:i + 1] in d:
            cache[i] = i + 1
        if cache[i] == -1:
            for j in range(len(i)):
                if (cache[j] != 0 and s[j + 1:i + 1] in d):
                    cache[i] = i - j
                    break
    ret = []
    if cache[-1] != -1:
        id = len(s) - 1
        while id >= 0:
            ret.append(s[id - cache[id] + 1:id + 1])
            id -= cache[id]
        ret.reverse()
    return ret
