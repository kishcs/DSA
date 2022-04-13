def solution(X, A):
    store = set()
    count = 0
    for i in A:
        if i in store:
            continue
        else:
            store.add(i)
            count += 1
            if count == X:
                return A.index(i)
    return -1


if __name__ == "__main__":
    X = 5
    A = [1, 3, 1, 4, 2, 3, 5, 4]
    time = solution(X, A)
    print(time)