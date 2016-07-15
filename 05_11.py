# Rectangle intersection
class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

def rectangle_intersection(r1, r2):
    ret_r = Rectangle(
        max(r1.x, r2.x),
        max(r1.y, r2.y),
        min(r1.x + r1.w, r2.x + r2.w) - max(r1.x, r2.x),
        min(r1.y + r1.h, r2.y + r2.h) - max(r1.y, r2.y))
    if ret_r.w < 0 or ret.h < 0:
        return (0, 0, -1, -1)
    else:
        return ret_r
