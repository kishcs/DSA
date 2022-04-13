# https://app.codility.com/c/feedback/854ZD9-AMX/
import time


# time taken: 8154603300
# 799999
def solution(S):
    ops = 0
    a = int(S, 2)
    # print(a)
    while a:
        if a & 1:  # odd
            a -= 1  # if in even case you are going to shift, then no need to do minus 1
            # e.g. 11101 >> 1 is same as 11100 >> 1
        else:
            a >>= 1  # even so divide by 2.. same as right shift
        ops += 1
    print('==>', ops)
    return ops


# time taken: 4603804400
# 799999
def solution1(S):  # 100% Solution
    ops = 0
    a = int(S, 2)
    while a:
        if 1 < a and a & 1:
            ops += 1
        a >>= 1
        ops += 1
        print(a)
    return ops


if __name__ == "__main__":
    # s = '1111010101111'
    s = '1' * 400000
    # s = '11100'
    # op = solution1(s)
    # print(op)
    # print(2>>1, 1>>1)

    start = time.time_ns()
    op = solution(s)
    print('time taken:', (time.time_ns() - start))
    print(op)

    start = time.time_ns()
    op = solution1(s)
    print('time taken:', (time.time_ns() - start))
    print(op)

    # print(int('11100', 2), int('11101', 2), 28>>1, 29>>1)
    # print(6 >> 1, 7 >> 1)
