# Render a calendar.
def find_max_concurrent(l_events):
    l_times = []
    for e in l_events:
        l_times.append((e[0], 0))
        l_times.append((e[1], 1))
    l_times.sort()
    ret, cur_sum = 0, 0
    for t in l_times:
        if t[0] == 0:
            cur_sum += 1
            ret = max(ret, cur_sum)
        else:
            cur_sum -= 1
    return ret
