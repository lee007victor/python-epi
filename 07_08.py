# The look-and-say problem.
def look_and_say(n):
    s = '1'
    for _ in range(1, n):
        s = helper(s)
    return s

def helper(s):
    res = []
    i, cnt = 0, 1
    while i < len(s):
        if (i < len(s) - 1 and s[i] == s[i + 1]):
            cnt += 1
        else:
            res.append(str(cnt))
            res.append(s[i])
            cnt = 1
        i += 1
    return ''.join(res)

# Test.
test_cases = [8]
for case in test_cases:
    print look_and_say(case)
