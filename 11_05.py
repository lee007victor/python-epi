# Compute the median of online data.
import heapq

def online_median(iter_n):
    min_h = []
    max_h = []
    curr = next(iter_n, None)
    # Be careful using 'while curr' because curr maybe 0
    while curr is not None:
        if not min_h:
            heapq.heappush(min_h, curr)
        else:
            if curr >= min_h[0]:
                heapq.heappush(min_h, curr)
            else:
                heapq.heappush(max_h, -curr)
        if len(min_h) > len(max_h) + 1:
            heapq.heappush(max_h, -heapq.heappop(min_h))
        elif len(min_h) < len(max_h):
            heapq.heappush(min_h, -heapq.heappop(max_h))
        cur_m = (min_h[0] if len(min_h) > len(max_h) else
            0.5*(min_h[0]-max_h[0]))
        print cur_m
        curr = next(iter_n, None)

# Test.
test_cases = [
    (1, 0, 3, 5, 2, 0, 1),
    ]

for case in test_cases:
    online_median(iter(case))
