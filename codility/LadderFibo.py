import math


# 37%
# (34, 'Numerical result out of range')
# WRONG ANSWER, got [0, 2, 7111, 1597, 0,.. expected [1729, 2, 7106, 1597,..
def solution(A, B):
    L = len(A)
    result = [0] * L
    for i in range(L):
        c = math.sqrt(5)
        a = ((1 + c) / 2) ** (A[i] + 1)
        b = ((1 - c) / 2) ** (A[i] + 1)
        f = (a - b) / c
        result[i] = int(f) & (2 ** B[i]-1)
    return result


# https://app.codility.com/demo/results/trainingA3UH3H-3QG/
# 87%, O(L**2)
# TIMEOUT ERROR, running time: 1.160 sec., time limit: 0.784 sec.

# https://app.codility.com/demo/results/training2T8YRS-ZHN/
# O(L)
def solution1(A, B):
    m = max(A)+2
    fib = [0] * m
    fib[1] = 1
    for i in range(2, m):
        fib[i] = fib[i-1] + fib[i-2]
    print(fib)

    L = len(A)
    result = [0] * L

    for i in range(L):
        # result[i] = fib[A[i]+1] % pow(2, B[i])        # 87% Pass
        result[i] = fib[A[i] + 1] & (pow(2, B[i])-1)    # 100% Pass
    return result


if __name__ == '__main__':
    A = [4, 4, 5, 5, 1]
    B = [3, 2, 4, 3, 1]
    res = solution1(A, B)
    print(res)

    # p = 2**30
    # q = p + p//2
    # print(p, p-1)
    # print(q % p, q & (p-1))
    print(55 % 8, 55 & 7)
    # print(bin(15), bin(5))


# https://app.codility.com/demo/results/training3YXFAJ-C5Y/
'''
def solution(A, B):
    L = max(A)
    P_max = max(B)
 
    fib = [0] * (L+2)
    fib[1] = 1
    for i in xrange(2, L + 2):
        fib[i] = (fib[i-1] + fib[i-2]) & ((1 << P_max) - 1)
 
    return_arr = [0] * len(A)
 
    for idx in xrange(len(A)):
        return_arr[idx] = fib[A[idx]+1] & ((1 << B[idx]) - 1)
 
    return return_arr
'''

# https://app.codility.com/demo/results/trainingZDCWXJ-GX2/
'''
def solution(A, B):
    L = max(A)
 
    fib = [0] * (L+2)
    fib[1] = 1
    for i in xrange(2, L + 2):
        fib[i] = (fib[i-1] + fib[i-2]) % (1 << 30)
 
    return_arr = [0] * len(A)
 
    for idx in xrange(len(A)):
        return_arr[idx] = fib[A[idx]+1] & ((1 << B[idx]) - 1)
 
    return return_arr
'''