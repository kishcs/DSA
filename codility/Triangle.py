def solution(A): # O(N*log(N)), 100% Pass
    A.sort()
    s = len(A)
    for i in range(s):
        if i < s-2 and A[i] + A[i+1] > A[i+2]:
            print('At', i, '=>', A[i], A[i + 1], A[i + 2])
            return 1
    return 0


if __name__ == "__main__":
    # A = [10, 2, 5, 1, 8, 20]
    A = [-10, 15, 5, 11]
    can_be = solution(A)
    print(can_be)