# https://app.codility.com/c/feedback/854ZD9-AMX/
import time


def solution(S):
    ops = 0
    a = int(S, 2)
    while a:
        if a & 1:  # odd
            a -= 1
        else:
            a >>= 1  # even: divide by 2 => same as right shift
        ops += 1
    # print('==>', ops)
    return ops


def solution1(S):
    """
    In ODD case, reduce by 1, then in EVEN case divide by 2 (same as right shift by 1)
    If we will perform rightshift for next EVEN, then no need to reduce by 1 for prev ODD num.
    because right shifting N(i.e. ODD) with 1 bit is same as right shifting (N-1)(i.e. EVEN) with 1 bit
    e.g. 11101 >> 1 is same as 11100 >> 1, both ends up at 1110
    """
    ops = 0
    a = int(S, 2)
    while a:
        if a & 1 and a > 1:  # odd but not 1
            ops += 1
        a >>= 1
        ops += 1
        # print(a)
    return ops


def solution2(S):  # 100% Solution
    # Formula: ops = 2X-1+Y, X: No. of Ones, Y: No. of Zeros
    data = str(S)
    ones = data.count('1')
    zeros = data.count('0')
    # print(ones, zeros)
    return 2 * ones - 1 + zeros


def main():
    # s = '111101010111010'
    s = '1' * 1000000
    # s = '11100'

    start = time.time_ns()
    op = solution(s)
    print('time taken:', (time.time_ns() - start) / 1000000, 'ms')
    print(op)

    start = time.time_ns()
    op = solution1(s)
    print('time taken:', (time.time_ns() - start) / 1000000, 'ms')
    print(op)

    start = time.time_ns()
    op = solution2(s)
    print('time taken:', (time.time_ns() - start) / 1000000, 'ms')
    print(op)


def stressTest():
    data = ['1' * 400000, '1' * 600000, '1' * 800000, '1' * 1000000]
    # print(data)
    start = time.time_ns()
    for s in data:
        op = solution1(s)
        print(op)
    print('Total time taken:', (time.time_ns() - start) / 1000000, 'ms')

    start = time.time_ns()
    for s in data:
        op = solution2(s)
        print(op)
    print('Total time taken:', (time.time_ns() - start) / 1000000, 'ms')


if __name__ == "__main__":
    main()
    # stressTest()
