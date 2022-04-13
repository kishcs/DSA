def solution(A, B, C):
    N = len(A)
    M = len(C)
    nails = enumerate(C)  # sorted(enumerate(C), key=lambda var: var[1])
    X = [i for i in zip(A, B)]
    X.sort(key=lambda x: x[0])
    print(X)
    print(nails)
    i = 0
    max_index = -1;
    for c_index, c in nails:
        if max_index < c_index:
            max_index = c_index
            print('max_index:', max_index)
        print(c, 'in', (X[i][0], X[i][1]))
        while i < N and X[i][0] <= c <= X[i][1]:
            i += 1
        print(f'({i} == {N}) =>', i == N)
        if i == N:
            return max_index + 1
    return -1


# https://app.codility.com/demo/results/trainingKB4TKU-E3M/
# 25%
# https://app.codility.com/demo/results/trainingCUDNVZ-M7D/
# 62% O(N * M)
def solution1(A, B, C):
    N = len(A)
    M = len(C)
    # i = 0
    # c_index = 0
    latest_c_index = -1
    for i in range(N):
        c_index = 0
        # print('A:', A[i], 'B:', B[i], 'C:', C[c_index], (A[i] > C[c_index] > B[i]))

        while c_index < M:
            # print('A[i] <= C[c_index] <= B[i]', A[i] <= C[c_index] <= B[i])
            if A[i] <= C[c_index] <= B[i]:
                # print(c_index)
                if latest_c_index < c_index:
                    latest_c_index = c_index
                break
            else:
                if c_index >= M - 1:
                    return -1
                c_index += 1
                if latest_c_index < c_index:
                    latest_c_index = c_index

    # print('final:', latest_c_index + 1)
    return latest_c_index + 1


def solution2(A, B, C):
    N = len(A)
    M = len(C)

    latest_c_index = -1
    for i in range(N):
        c_index = 0
        # print('A:', A[i], 'B:', B[i], 'C:', C[c_index], (A[i] > C[c_index] > B[i]))

        while c_index < M:
            # print('A[i] <= C[c_index] <= B[i]', A[i] <= C[c_index] <= B[i])
            if A[i] <= C[c_index] <= B[i]:
                # print(c_index)
                if latest_c_index < c_index:
                    latest_c_index = c_index
                break
            else:
                if c_index >= M - 1:
                    return -1
                c_index += 1
                if latest_c_index < c_index:
                    latest_c_index = c_index

    # print('final:', latest_c_index + 1)
    return latest_c_index + 1


if __name__ == '__main__':
    A = [24, 11, 3, 7]  # [3, 1, 5]  # [10, 6, 3, 16] #[3, 1, 5]  #[1, 4, 5, 8]  #
    B = [25, 17, 5, 10]  # [5, 4, 9]  # [15, 9, 5, 20] #[4, 5, 9, 10]  #
    C = [9, 4, 12, 30, 24]  # [6, 2, 3, 11, 13] # [7, 17, 4, 12, 17, 22] #[10, 2, 3, 11, 13]  # [4, 6, 7, 10, 2]  #

    res = solution(A, B, C)
    print(res)

    # nails = sorted(enumerate(C), key=lambda var: var[1])
    # X = [i for i in zip(A, B)]
    # X.sort(key=lambda x: x[0])
    # print(X)
    # print(nails)

    # for x, y in X:
    #     print(x, y)
    # print(X[0][0], X[1][1])

    # for i, c in nails:
    #     print(c, 'at index ', i)

    # planks = [i for i in zip(A, B)]
    # print(planks)
    # planks_sorted = sorted(planks, key=lambda x: x[0])
    # print([i for i in planks_sorted])
    #
    # for i in enumerate(C):
    #     print(i, end=' ')
    # print()
    # nails = sorted(enumerate(C), key=lambda var: var[1])
    # print(nails)
