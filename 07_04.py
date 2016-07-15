# Replace and remove.
def replace_and_remove(string, n):
    w_i, cnt = 0, 0
    for i in range(n):
        if string[i] != 'b':
            string[w_i] = string[i]
            w_i += 1
        if string[i] == 'a':
            cnt += 1
    cur_i = w_i - 1
    w_i = w_i + cnt - 1
    while cur_i >= 0:
        if string[cur_i] == 'a':
            string[w_i] = 'd'
            w_i -= 1
            string[w_i] = 'd'
            w_i -= 1
        else:
            string[w_i] = string[cur_i]
            w_i -= 1
        cur_i -= 1

# Test.
cases = [
    [['a', 'b', 'a', 'c', None], 4],
    [['a', 'c', 'a', 'a', None, None, None], 4],
    ]

for c in cases:
    print c[0]
    replace_and_remove(c[0], c[1])
    print c[0]
