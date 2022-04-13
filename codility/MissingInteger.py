def solution(A):    # 77% Pass
    A.sort()
    A = list(set(A))

    if A[-1] <= 0:
        return 1
    if A[0] == 0:
        A = A[1:]
    if A[0] < 0:
        A = [i for i in A if i > 0]
    # print(A)
    for i in range(A[-1]):
        if i+1 != A[i]:
            return i+1
    return i+2


def solution1(A):   # 100% Pass, O(N) or O(N * log(N))
    A = list(set(A))
    A = [i for i in sorted(A) if i > 0]
    if not A:
        return 1
    # print(A)
    for i in range(A[-1]):
        if i+1 != A[i]:
            return i+1
    return i+2


if __name__ == "__main__":
    # arr = [1, 3, 6, 4, 1, 2]
    arr = [6, 4, 0, -1, -3, 1, 3, 2, 5]
    missing = solution1(arr)
    print(missing)
