#!/usr/bin/env python
import statistics
import time


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def show(self):
        print(self.stack)


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(30)
    s.show()
    s.push(20)
    s.push(50)
    s.show()
    print(s.peek(), s.size())
    s.pop()
    s.pop()
    s.push(40)
    s.show()
