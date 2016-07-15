# Find the nearest repeated entries in an array.
import sys

def find_nearest_repetition(p):
    words = {}
    ret = sys.maxint
    for i in range(len(p)):
        cur_word = p[i]
        if cur_word in words:
            ret = min(ret, i - words[cur_word])
        words[cur_word] = i
    return ret
