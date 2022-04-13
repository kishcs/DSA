#!/usr/bin/env python
from queue import Queue, PriorityQueue
from collections import deque

if __name__ == "__main__":
    q = Queue()
    dq = deque()
    # print(q, dq)
    dq.append(1)
    dq.append(5)
    dq.append(3)
    dq.append(6)
    dq.append(2)
    dq.append(7)
    print(len(dq), dq)


