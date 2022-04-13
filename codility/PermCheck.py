def solution(A):
    size = len(A)
    should_be = size * (size+1) // 2
    actual = sum(A)
    if actual != should_be:
        return 0
    else:
        # if any element repeated then return 0
        # else return 1
        seen = set()
        for i in A:
            if i in seen:
                return 0
            else:
                seen.add(i)
        return 1


if __name__ == '__main__':
    A = [8, 4, 5, 1, 2, 2, 6, 8]
    stat = solution(A)
    print(stat)