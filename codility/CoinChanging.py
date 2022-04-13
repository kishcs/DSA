def solution(A, T):
    # NA = [[1 if col == 0 else 0 for col in range(T)] for _ in range(len(A))]
    # print(NA)
    mat = [[0] * (T + 1) for i in range(len(A))]
    mat[0] = [i for i in range(T + 1)]
    # print(len(mat))
    # for i in mat:
    #     print(i)

    for i in range(1, len(mat)):
        # print('for', A[i])
        for j in range(1, len(mat[0])):
            if j < A[i]:
                mat[i][j] = mat[i - 1][j]
            else:
                mat[i][j] = min(1 + mat[i][j - A[i]], mat[i - 1][j])
            # print(mat[i][j], end=' ')
        # print()
    # ind = -1
    for i in mat:
        # ind += 1
        # print(A[ind], '=>', i)
        print(i)
    return 0


if __name__ == '__main__':
    arr = [1, 3, 4] # [1, 5, 6, 8]
    T = 6 # 11
    min_count = solution(arr, T)
    print(min_count)
