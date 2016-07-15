# Implement an ISBN cache.
import collections

class LruCache:
    def __init__(size):
        self.size = size
        sefl.dict = collections.OrderedDict([])

    def lookup(k):
        if k not in self.dict:
            return None
        v = self.dict[k]
        del self.dict[k]
        self.dict[k] = v
        return v

    def insert(k, v):
        if k in self.dict:
            old_v = self.dict[k]
            del self.dict[k]
            self.dict[k] = old_v
        else:
            self.dict[k] = v
        if len(self.dict) >= 2 * self.size:
            for _ in range(len(self.dict) - self.size):
                cur_key = self.dict.items()[0][0]
                del self.dict[cur_key]

    def erase(k):
        if k in self.dict:
            return self.dict.pop(k)
