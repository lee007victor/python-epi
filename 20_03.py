"""
# Solution 1: using lock
import threading

class MyThread(threading.Thread):
    def __init__(self, is_odd, counter):
        threading.Thread.__init__(self)
        self.is_odd = is_odd
        self.counter = counter 
    def run(self):
        while self.counter.running:
            self.counter.increment(self.is_odd)

class Counter:
    def __init__(self, max_cnt):
        self.lock = threading.Lock()
        self.cnt = 0
        self.max_cnt = max_cnt
        self.running = True

    def increment(self, is_odd):
        self.lock.acquire()
        if self.cnt < self.max_cnt:
            if ((is_odd and self.cnt % 2 == 0) or 
               (not is_odd and self.cnt % 2 != 0)):
                    self.cnt += 1
                    print self.cnt
        else:
            self.running = False
        self.lock.release()

counter = Counter(100)
thread_odd = MyThread(True, counter)
thread_even = MyThread(False, counter)
thread_odd.start()
thread_even.start()

thread_odd.join()
thread_even.join()
"""

# Solution 2: using condition
import threading

class OddEvenMonitor:
    def __init__(self, turn_flag, cv):
        self.turn_flag = True
        self.cv = cv
    def wait_turn(self, my_turn):
        self.cv.acquire()
        while self.turn_flag != my_turn: 
            self.cv.wait()
    def toggle_turn(self):
        self.turn_flag ^= True
        self.cv.notify()
        self.cv.release()

def printer(is_odd, monitor):
    start = 1 if is_odd else 2
    end = 100 if is_odd else 101
    for i in range(start, end, 2):
        monitor.wait_turn(is_odd)
        print i
        monitor.toggle_turn()

monitor = OddEvenMonitor(True, threading.Condition())
thread_odd = threading.Thread(target=printer, args=(True, monitor))
thread_even = threading.Thread(target=printer, args=(False, monitor))
thread_odd.start()
thread_even.start()
thread_odd.join()
thread_even.join()

"""
# Solution 3: using condition
import threading

cur_num = 0

def odd_even_printer(max_num, is_odd, cv):
    global cur_num
    while cur_num < max_num:
        with cv:
            while ((is_odd and cur_num % 2 != 0) or 
                    (not is_odd and cur_num % 2 == 0)):
                cv.wait()
            if cur_num < max_num:
                cur_num += 1
                print cur_num
            cv.notify()

cv = threading.Condition()
thread_odd = threading.Thread(target=odd_even_printer, args=(10, True, cv))
thread_even = threading.Thread(target=odd_even_printer, args=(10, False, cv))
thread_odd.start()
thread_even.start()
thread_odd.join()
thread_even.join()
"""
