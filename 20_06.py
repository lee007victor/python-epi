"""
# Solution 1: two condition variables
import threading

class ReadLock:
    def __init__(self, wl):
        self.wl = wl
        self.cnt = 0
        self.cv = threading.Condition()
    def lock(self):
        self.wl.cv.acquire()
            while self.wl.in_writing:
                self.wl.cv.wait()
        with self.cv:
            self.cnt += 1
    def release(self):
        with self.cv:
            self.cnt -= 1
            self.cv.notifyAll()
        self.wl.cv.release()

class WriteLock:
    def __init__(self, rl): # rl for read lock
        self.rl = rl
        self.cv = threading.Condition()
        self.in_writing = False
    def lock(self):
        self.cv.acquire():
            while self.cv.in_writing:
                self.cv.wait()
        self.rl.cv.acquire():
            while self.rl.cnt != 0:
                self.rl.cv.wait()
    def release(self):
        self.rl.cv.release()
        self.in_writing = False
        self.cv.notifyAll()
        self.cv.release()

class Reader(threading.Thread):
    def __init__(self, rl):
        threading.Thread.__init__(self)
        self.rl = rl
    def run(self):
        while not exit_flag:
            self.rl.lock()
            do_reading()
            self.rl.release()

class Writer(threading.Thread):
    def __init__(self, rl, wl):
        threading.Thread.__init__(self)
        self.wl = wl
    def run(self):
        while not exit_flag:
            self.wl.lock()
            do_writing()
            self.wl.release()

def do_some_reading():
    pass

def do_some_writing():
    pass

exit_flag = False
rl = ReadLock()
wl = WriteLock(rl)
thread_reader = Reader()
thread_writer = Writer()
thread_reader.start()
thread_writer.start()
thread_reader.join()
thread_writer.join()
"""

# Solution 2: one condition variable and one lock
import threading

class ReadWriteLock:
    def __init__(self):
        self.cnt = 0
        self.cv = threading.Condition()
        self.wl = threading.Lock()
    def read_lock(self):
        with self.cv:
            self.cnt += 1
    def read_release(self):
        with self.cv:
            self.cnt -= 1
            self.cv.notify_all()
    def write_lock(self):
        self.wl.acquire()
        self.cv.acquire()
        while self.cnt != 0:
            self.cv.wait()
    def write_release(self):
        self.cv.release()
        self.wl.release()

class Reader(threading.Thread):
    def __init__(self, rw):
        threading.Thread.__init__(self)
        self.rw = rw
    def run(self):
        self.rw.read_lock()
        do_reading()
        self.rw.read_release()

class Writer(threading.Thread):
    def __init__(self, rw):
        threading.Thread.__init__(self)
        self.rw = rw
    def run(self):
        self.rw.write_lock()
        do_writing()
        self.rw.write_release()

def do_reading():
    pass

def do_writing():
    pass

rw = ReadWriteLock()
thread_reader = Reader(rw)
thread_writer = Writer(rw)
thread_reader.start()
thread_writer.start()
thread_reader.join()
thread_writer.join()
