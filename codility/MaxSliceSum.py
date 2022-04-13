import sys


def solution(A):
    if len(A) == 1:
        return A[0]
    max_sum = -sys.maxsize
    curr_sum = 0
    for i in A:
        curr_sum += i
        if max_sum < curr_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice


if __name__ == '__main__':
    # A = [4, -8, 3, -1, 5]
    A = [-8, -7, -6, -4, -1]
    # A = [9]
    s = solution(A)
    print(s)


