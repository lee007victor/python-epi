# Computer x^y

def power(x, y):
    ret = 1
    if y < 0:
        y = -y
        x = 1.0 / x
    while y:
        if (y & 1):
            ret *= x
        x *= x
        y >>= 1
    return ret

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
points = [
    Point(0, 0),
    Point(0, 1),
    Point(1.1, 21),
    Point(1.1, -21),
    ]
for p in points:
    print power(p.x, p.y)
