# Find the majority element.
def majority_search(iter_str):
    cand = None
    cur_str, cnt_cand = next(iter_str, None), 0
    while cur_str:
        if cnt_cand == 0:
            cand = cur_str
            cnt_cand = 1
        elif cur_str == cand:
            cnt_cand += 1
        else:
            cnt_cand -= 1
        cur_str = next(iter_str, None)
    return cand

# Test.
case = [2,1,3,1,1,2,1,1,3,1]
print majority_search(iter(case))
