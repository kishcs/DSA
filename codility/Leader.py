def solution(A):
    store = {}
    max_count = 0
    leader = None
    for i in A:
        count = store.get(i, 0)
        store[i] = count + 1
        if max_count < store[i]:
            max_count = store[i]
            leader = i
    if max_count > len(A) / 2:
        return leader
    return -1


if __name__ == '__main__':
    A = [3, 4, 3, 2, 3, -1, 3, 3]  # [3, 4, 4, 1, 4, 2, 4, 5, 4]  # [6, 4, 6, 8, 6, 8, 6]
    l = solution(A)
    print(l)
