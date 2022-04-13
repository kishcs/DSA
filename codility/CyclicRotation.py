import time


def solution(A, K):
    length = len(A)
    if length == 0 or K == length:
        return A
    elif K < length:
        return A[length-K:] + A[:length-K]
    else:
        # K -= length
        K %= length
        return solution(A, K)


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    K = 200007
    start = time.time()
    R = solution(A, K)
    diff = time.time() - start
    print(R)
    print(diff)

    # arr = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    # print(arr.count(1), len(arr))

    # result = all(element == arr[0] for element in arr)
    # print(result)
