# Merge sorted lists

from heapq import heappush, heappop

def merge_sorted_lists(lists):
    # data structure: returned list, min heap, and a head list
    ret_list, min_hp, heads = [], [], []

    # push each list's 1st element in the min heap
    for i in range(len(lists)):
        if len(lists[i]) > 0:
            heappush(min_hp, (list[i][0], i))
            heads.append(1)
        else:
            heads.append(0)

    while min_hp:
        n, i = heappop(min_hp)
        ret_list.append(n)
        j = heads[i]
        if j < len(lists(i)):
            heappush(min_hp, (list[i][j], i))
            heads[i] += 1

    return ret_list
