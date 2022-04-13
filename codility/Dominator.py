def solution(A):
    store = {}
    # indices = {}
    max_count = 0
    leader = None

    for i in range(len(A)):
        count = store.get(A[i], 0)
        store[A[i]] = count + 1
        # indices[A[i]] = indices.get(A[i], []) + [i]
        if max_count < store[A[i]]:
            max_count = store[A[i]]
            leader = A[i]
    if max_count > len(A) / 2:
        # return indices[leader]
        return A.index(leader)
    return -1


if __name__ == '__main__':
    A = [3, 4, 3, 2, 3, -1, 3, 3]
    # A = [3, 4, 4, 1, 4, 2, 4, 5, 4]
    # A = [6, 4, 6, 8, 6, 8, 6]
    l = solution(A)
    print(l)
