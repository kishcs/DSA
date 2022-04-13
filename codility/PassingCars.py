import sys


def solution(A):
    # size = len(A)
    ones = A.count(1)
    count = 0
    for i in A:
        if i == 0:
            count += ones
        else:
            ones -= 1
    return -1 if count > 1000000000 else count


if __name__ == "__main__":
    arr = [0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0]
    pairs = solution(arr)
    print(pairs)
    sys.exit(0)
