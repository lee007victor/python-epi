# Compute the union of intervals.
class Point:
    def __init__(self, val, is_closed):
        self.val = val 
        self.is_closed = is_closed

class Interval:
    def __init__(self, lp, rp):
        self.lp = lp
        self.rp = rp
    def __lt__(self, other):
        if self.lp.val < other.lp.val:
            return True
        elif (self.lp.val == other.lp.val and 
                self.lp.is_closed and not other.lp.is_closed):
            return True
        else:
            return False
    def __gt__(self, other):
        if self.lp.val > other.lp.val:
            return True
        elif (self.lp.val == other.lp.val and
                not self.lp.is_closed and other.lp.is_closed):
            return True
        else:
            return False
    def __eq__(self, other):
        return (self.val == other.val and 
                not (self.is_closed ^ other.is_closed))
    def __ne__(self, other):
        return not self.__eq__(other)
    def __le__(self, other):
        return (self.__lt__(other) or self.__eq__(other))
    def __ge__(self, other):
        return (self.__gt__(other) or self.__eq__(other))

def interval_union(a):
    if not a:
        return None
    a.sort()
    ret, curr = [], a[0]
    for it in a[1:]:
        if (it.lp.val < curr.rp.val 
                or (it.lp.val == curr.rp.val
                    and (it.lp.is_closed or it.rp.is_closed))):
            if (it.rp.val > curr.rp.val
                    or (it.rp.val == curr.rp.val
                        and it.rp.is_closed)):
                curr.rp = it.rp 
        else:
            ret.append(curr)
            curr = it
    ret.append(curr)
    return ret
