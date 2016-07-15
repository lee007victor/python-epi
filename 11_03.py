# Sort an almost-sorted array
import heapq

def sort_data(iter_n, k):
    h = []
    for i in range(k):
        cur_num = next(iter_n, None)
        if cur_num:
            heapq.heappush(h, cur_num)

    cur_num = next(iter_n, None)
    while cur_num:
        heapq.heappush(h, cur_num)
        print heapq.heappop(h),
        cur_num = next(iter_n, None)

    while h:
        print heapq.heappop(h),
        
# Test.
list_nums = [3, -1, 2, 6, 4, 5, 8]
sort_data(iter(list_nums), 2)
