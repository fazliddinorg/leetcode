from typing import List
import threading

# SOLUTION 1: Using Locks
# Time: Depends on thread scheduling, Space: O(1)
class Foo1:
    def __init__(self):
        self.lock2 = threading.Lock()
        self.lock3 = threading.Lock()
        self.lock2.acquire()
        self.lock3.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.lock2.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.lock2:
            printSecond()
            self.lock3.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.lock3:
            printThird()



# SOLUTION 2: Using Events
# Time: Depends on thread scheduling, Space: O(1)
class Foo2:
    def __init__(self):
        self.event2 = threading.Event()
        self.event3 = threading.Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.event2.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.event2.wait()
        printSecond()
        self.event3.set()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.event3.wait()
        printThird()