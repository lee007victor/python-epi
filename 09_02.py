# Evaluate RPN expressions
def eval_rpn(s):
    ops = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        'x': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        }
    l_s = s.split(',')
    buf = []
    for c in l_s:
        if c in ops:
            y = buf.pop()
            x = buf.pop()
            buf.append(ops[c](x, y))
        else:
            buf.append(int(c))
    return buf.pop()

# Test.
test_cases = [
    '1729',
    '3,4,+,2,x,1,+',
    '1,1,+,-2,x',
    '-641,6,/,28,/',
    ]

for t in test_cases:
    print eval_rpn(t)
