import sys


def solution1(A, B, K): # O(1), 100% Pass
    # write your code in Python 3.6
    if K > B:
        return 0 if A > 0 else 1
    count = 0
    first = -1
    if A % K == 0:
        first = A
    else:
        rem = A % K
        first = A + K - rem
    last = K * (B // K)
    count = (last//K) - (first//K) + 1
    return count


def solution(A, B, K):
    if K > B:
        return 0 if A > 0 else 1
        # if A <= K <= B:
    count = 0
    first = -1
    if A % K == 0:
        first = A
    else:
        rem = A % K
        first = A + K - rem
    # print('FIRST', first)
    # for i in range(A, B+1):
    #     if i % K == 0:
    #         first = i
    #         break
    last = K * (B // K)
    print(first, 'and', last)
    # print(first // K, 'and', last // K)

    # if first == -1:
    #     return 0
    count = (last//K) - (first//K) + 1
    # print('==>', checkthis)
    # count = len([i for i in range(first, last+1, K)])
    return count


if __name__ == "__main__":
    A = 3
    B = 15 # 2000000000
    K = 6
    total = solution(A, B, K)
    print(total)

    # print(sys.maxsize)
    # print(2**63-1)
    sys.exit(0)
