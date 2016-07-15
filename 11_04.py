# Compute the k closest stars.
import heapq

def find_k_closest_stars(k, stars):
    h = []
    cur_star = next(stars, None)
    while cur_star:
        heapq.heappush(h, (-dist_earth(star), star))
        if len(h) > k:
            heapq.heappop(h)
        cur_star = next(stars, None)
    h.sort(key=lambda x: -x[0])
    return [x[1] for x in h]

def dist_earth(p):
    return (p[0]**2 + p[1]**2 + p[2]**2) ** 0.5
