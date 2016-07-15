# EPI 7.1 Interconvert strings and integers

def IntToString(i):
    neg = True if i < 0 else False
    i = abs(i)
    s = ''
    while True:
        s += str(i%10)
        i /= 10
        if i == 0:
            break
    return '-' + s[::-1] if neg else s[::-1]

def StringToInt(s):
    neg = True if s[0] == '-' else False
    i = 0
    for j in range(len(s)):
        if j == 0 and s[j] == '-':
            continue
        i = i*10 + int(s[j])
    return -i if neg else i

# Unit test
test_int_to_str = [
    (0, '0'),
    (1, '1'),
    (-1, '-1'),
    (123, '123'),
    (-123, '-123'),
    ]

test_str_to_int = [
    ('0', 0),
    ('1', 1),
    ('-1', -1),
    ('123', 123),
    ('-123', -123),
    ]

def Test():
    for t in test_int_to_str:
        print 'Input: {} Result: {}'.format(
            t[0], 'Correct' if IntToString(t[0]) == t[1] else 'Wrong')
    for t in test_str_to_int:
        print 'Input: {} Result: {}'.format(
            "'" + t[0] + "'", 'Correct' if StringToInt(t[0]) == t[1] else 'Wrong')

Test()

