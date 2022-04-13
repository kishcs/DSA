def solution(A):
    store = {}
    target = []

    # Third way -- Timeout Error
    # for i in A:
    #     if A.count(i) % 2 != 0:
    #         return i

    # Second way -- Timeout Error
    # for i in A:
    #     count = store.get(i, 0)
    #     store[i] = count + 1
    #     if (count + 1) % 2 != 0:
    #         target.append(i)
    #     else:
    #         target.remove(i)
    # print(store)
    # return target[0]

    # First way -- Passed O(N) or O(N*log(N))
    for i in A:
        count = store.get(i, 0)
        store[i] = count + 1

    # for k, v in map.items():
    #     if v % 2 != 0:
    #         return k

    # val = [k for k, v in sorted(store.items(), key=lambda item: item[1]) if v % 2 != 0]
    val = [k for k, v in sorted(store.items()) if v % 2 != 0]
    # print(val)
    return val[0]


def main():
    A = [9, 3, 9, 4, 3, 4, 7, 5, 7, 5, 7, 7, 9, 7, 9]
    odd = solution(A)
    print(odd)


if __name__ == "__main__":
    main()