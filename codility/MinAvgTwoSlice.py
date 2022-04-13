import sys


def solution1(A):    #Timeout, 50% Pass, O(N**3)
    s = len(A)
    # print('size:', s, A)
    pos = -1
    min_avg = sys.maxsize
    for i in range(s - 1):
        for j in range(i+2, s+1):
            print(A[i:j], end=' ')
            avg = sum(A[i:j])/(j-i)
            if min_avg > avg:
                min_avg = avg
                pos = i
            # print(avg,'=>', i, end=' ')
        print()
    return pos


def solution(A): #O(N), 100% Pass
    pos = 0
    min_val = 10001
    s = len(A)
    for i in range(0, s - 1):
        if (A[i] + A[i + 1]) / 2.0 < min_val:
            pos = i
            min_val = (A[i] + A[i + 1]) / 2.0
        if i < s - 2 and (A[i] + A[i + 1] + A[i + 2]) / 3.0 < min_val:
            pos = i
            min_val = (A[i] + A[i + 1] + A[i + 2]) / 3.0

    return pos


if __name__ == '__main__':
    # A = [1, 5, 3, 5, 2, 7]
    A = [1, 5, 3, 5, 2, 7, 9, 1, 2, 7, 1, 3, 1, 1, 7, 9, 0]
    index = solution(A)
    print(index)
