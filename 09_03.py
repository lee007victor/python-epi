# Test a string over '{,},(,),[,]' for well-formedness
def is_well_formed(s):
    buf = []
    r2l = {')':'(', '}':'{', ']':'['}
    for c in s:
        if c in r2l.values():
            buf.append(c)
        else:
            if not buf:
                return False
            if buf.pop() != r2l[c]:
                return False
    return not buf
