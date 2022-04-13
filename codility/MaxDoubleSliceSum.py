import sys


def solution(A):
    s = len(A)
    if s == 3:
        return 0
    left = [0] * s
    right = [0] * s

    for i in range(1, s):
        left[i] = max(0, A[i] + left[i-1])
    for i in range(s-1)[::-1]:
        # print(i, end=' ')
        right[i] = max(0, right[i+1] + A[i])
    # print(left, right)
    max_sum = 0
    for i in range(1, s-1):
        max_sum = max(max_sum, left[i-1] + right[i+1])
    return max_sum


def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice


def max_double_slice(A):
    s = len(A)
    ending_here = [0] * s
    starting_here = [0] * s

    for i in range(1, s):
        ending_here[i] = max(0, ending_here[i - 1] + A[i])

    for i in reversed(range(s - 1)):
        starting_here[i] = max(0, starting_here[i + 1] + A[i])

    # print(ending_here, starting_here)

    max_double_slice_sum = 0

    for i in range(1, s - 1):
        # print(starting_here[i + 1], ending_here[i - 1])
        max_double_slice_sum = max(max_double_slice_sum, starting_here[i + 1] + ending_here[i - 1])

    return max_double_slice_sum


if __name__ == '__main__':
    # A = [4, -8, 3, -1, 5]
    # A = [-8, -7, -6, -4, -1]
    A = [3, 2, 6, -1, 4, 5, -1, 2]
    s = solution(A)
    print(s)

    # for i in reversed(range(7)):
    #     print("==>", i)
    # for i in range(7)[::-1]:
    #     print("==>", i)

