#!/usr/bin/env python
import math
import statistics
import time


class Node:
    def __init__(self, val=0, n=None):
        self.val = val
        self.next = n


def fib(n):
    a = 0
    b = 1
    while a <= n:
        print(a, end=' ')
        c = a + b
        a = b
        b = c


def fibo(n):
    for i in range(n):
        # root = math.sqrt(5)
        a = ((1 + math.sqrt(5)) / 2) ** i
        b = ((1 - math.sqrt(5)) / 2) ** i
        c = math.sqrt(5)
        f = (a - b) / c
        # if int(f) >= n:
        #     break
        print(int(f), end=' ')



def printList(head: Node):
    while head != None:
        print(head.val, end=' ')
        head = head.next


def insert_first(head, val):
    n = Node(val)
    if head == None:
        return n
    else:
        n.next = head
        head = n
        return head


def insert(head, val):
    n = Node(val)
    if head == None:
        head = n
        return head
    while head.next != None:
        head = head.next
    head.next = n


def divisors(n):
    i = 1
    result = 0
    while i * i < n:
        # print('i:', i)
        if n % i == 0:
            result += 2
        i += 1
    if i * i == n:
        result += 1
    return result


def primality(n):
    i = 2
    while (i * i <= n):
        if (n % i == 0):
            return False
        i += 1
    return True


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)


def lcm(a, b):
    return (a * b) / gcd(a, b)


if __name__ == "__main__":
    # Divisor and Prime
    # res = divisors(9)
    # print(res)
    # print('727', primality(727))

    # GCD, LCM
    # print(gcd(21, 14))
    # print(lcm(21, lcm(14, 7)))
    # print(lcm(35, 7))

    # fibo(14)
    # print()
    # fib(250)
    # print()
    # print(123%16, 123&15, 123 & ((1<<4)-1))
    # print(2**4, bin(2**4), 1<<4)
    # print(2 ** 30, 1 << 30)

    l1 = ["eat", "sleep", "repeat"]
    s1 = "geek"
    # creating enumerate objects
    obj1 = enumerate(l1)
    obj2 = enumerate(l1, 3)
    obj3 = enumerate(s1)
    obj4 = enumerate(s1, 2)

    print("Return type:", type(obj1))
    print(list(obj1))
    print(list(obj2))
    # changing start index to 2 from 0
    print(list(obj3))
    print(list(obj4))

    X = [[0]*4 for i in range(5)]
    print(X)
    X[0] = [0] + [5465] + [1000] * 2
    X[1] = [1] + [2] + [4]
    X[2] = [100]
    print(X)
    X[0] = [0] + [1000] * 3
    X[1] = [0] * 4
    X[2] = [0] * 4
    print(X)


    # LInked List
    # head = None
    # head = insert(head, 234)
    # insert(head, 330)
    # insert(head, 500)
    # printList(head)
    # print()

    # Average
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # print(A, sum(A)/len(A), statistics.mean(A))
    # A = [i for i in A if i%2==0]
    # print(A, sum(A)/len(A), statistics.mean(A))
    # l = [15, 18, 2, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 15, 18, 2, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 15, 18, 2, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 15, 18, 2, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 15, 18, 2, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 15, 18, 2, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 15, 18, 2, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78, 36, 12, 78, 5, 6, 9, 18, 2, 36, 12, 78]
    #
    # start = time.time_ns()
    # print('AVG[sum/len]:', sum(l)/len(l))
    # print(time.time_ns() - start)
    #
    # start = time.time_ns()
    # print('AVG[mean]:', statistics.mean(l))
    # print(time.time_ns() - start)
    #
    # start = time.time_ns()
    # print('AVG[fmean]:', statistics.fmean(l))
    # print(time.time_ns() - start)

    A=[]
    if not A:
        print(A)
    else:
        print(A, 'is empty')

    # PRIME




